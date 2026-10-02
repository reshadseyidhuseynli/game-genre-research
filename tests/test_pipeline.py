import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock
import requests
from src.common.config import load_game
from src.common.http import get_json
from src.common.io import read_jsonl, write_text, sha256
from src.collectors.steam_metadata import normalize_metadata
from src.collectors.steam_reviews import collect, validate
from src.processors.clean_reviews import normalize, samples
from src.processors.deduplicate import deduplicate
from src.processors.segment_reviews import segment
from src.processors.statistics import calculate

GAME = {'key': 'fixture', 'name': 'Fixture', 'steam_app_id': 1, 'request_delay_seconds': 1, 'sample_size': 50}


def review(identifier='1', **extra):
    return {'recommendationid': identifier, 'language': 'english', 'review': 'Good game!',
            'timestamp_created': 100, 'timestamp_updated': 200, 'voted_up': True,
            'author': {'playtime_at_review': 60}, **extra}


class DeterministicTests(unittest.TestCase):
    def test_config(self):
        self.assertEqual(load_game('hacknet')['steam_app_id'], 365450)
        with self.assertRaises(ValueError):
            load_game('missing')

    def test_invalid_config(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'games.yaml'
            path.write_text('games:\n  - key: ../bad\n    name: Bad\n    steam_app_id: 1\n')
            with self.assertRaises(ValueError):
                load_game('../bad', path)

    def test_normalization_preserves_original(self):
        original = '  Great\n game!\x00\tYes.  '
        row = normalize(review(review=original), GAME)
        self.assertEqual(row['review_text_raw'], original)
        self.assertEqual(row['review_text_clean'], 'Great game! Yes.')
        self.assertEqual(row['review_length_words'], 3)
        self.assertTrue(row['is_very_short'])
        self.assertEqual(row['playtime_at_review_hours'], 1)
        self.assertEqual(row['created_at'], '1970-01-01T00:01:40+00:00')
        self.assertEqual(row['overall_sentiment'], 'positive')
        self.assertIsNone(row['refunded'])
        self.assertIsNone(row['author_num_games_owned'])

    def test_missing_and_false(self):
        row = normalize(review(review='', voted_up=False, author={}, refunded=False), GAME)
        self.assertTrue(row['is_empty'])
        self.assertEqual(row['overall_sentiment'], 'negative')
        self.assertEqual(row['playtime_segment'], 'unknown')
        self.assertIs(row['refunded'], False)
        self.assertIsNone(normalize(review(voted_up=None), GAME)['overall_sentiment'])

    def test_segment_boundaries(self):
        for minutes, expected in [(None, 'unknown'), (-1, 'unknown'), (0, '0-1h'), (59, '0-1h'),
                                  (60, '1-3h'), (179, '1-3h'), (180, '3-10h'), (599, '3-10h'), (600, '10h+')]:
            self.assertEqual(segment(minutes), expected)

    def test_dedup_latest_and_tie(self):
        old = normalize(review(timestamp_updated=100), GAME)
        new = normalize(review(review='new'), GAME)
        rows, removed = deduplicate([new, old, new])
        self.assertEqual(removed, 2)
        self.assertEqual(rows, [new])

    def test_statistics_missing_denominators(self):
        rows = [normalize(review(votes_up=4), GAME),
                normalize(review('2', voted_up=False, author={'playtime_at_review': 180}, votes_up=2), GAME),
                normalize(review('3', voted_up=None, author={}), GAME)]
        stats = calculate(rows, 4)
        self.assertEqual(stats['duplicates_removed'], 1)
        self.assertEqual(stats['positive_ratio'], 1 / 3)
        self.assertEqual(stats['median_playtime_at_review'], 2)
        self.assertEqual(stats['average_playtime_negative'], 3)
        self.assertEqual(stats['average_votes_up_positive'], 4)
        self.assertIsNone(stats['positive_ratio_by_playtime_segment']['0-1h'])
        self.assertIsNone(calculate([], 0)['positive_ratio'])

    def test_sample_order(self):
        rows = [normalize(review('1', votes_up=2), GAME), normalize(review('2', votes_up=9, timestamp_created=300), GAME)]
        selected = samples(rows, 1)
        self.assertEqual(selected['helpful_positive'][0]['review_id'], '2')
        self.assertEqual(selected['recent_positive'][0]['review_id'], '2')
        self.assertEqual(len(selected['helpful_negative']), 0)

    def test_metadata_missing_price(self):
        result = normalize_metadata({'1': {'data': {'name': 'Fixture'}}}, GAME)
        self.assertIsNone(result['price'])
        self.assertIsNone(result['currency'])

    def test_raw_immutable(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'raw.json'
            write_text(path, 'original', immutable=True)
            with self.assertRaises(ValueError):
                write_text(path, 'changed', immutable=True)
            self.assertEqual(path.read_text(), 'original')


class CollectorTests(unittest.TestCase):
    def test_resume_pagination_and_idempotence(self):
        page1 = {'response': {'reviews': [review()], 'cursor': 'next', 'total_matching': 1}}
        end = {'response': {'reviews': []}}
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            failing = Mock(side_effect=[page1, RuntimeError('interrupted')])
            with self.assertRaises(RuntimeError):
                collect(GAME, root, fetch=failing, sleep=lambda _: None)
            fetch = Mock(return_value=end)
            result = collect(GAME, root, fetch=fetch, sleep=lambda _: None)
            self.assertEqual(fetch.call_count, 1)
            self.assertEqual(json.loads(fetch.call_args.args[1]['input_json'])['cursor'], 'next')
            self.assertEqual(result['raw_reviews'], 1)
            raw = root / 'raw/fixture/steam_reviews.jsonl'
            self.assertEqual(read_jsonl(raw)[0]['review'], 'Good game!')
            before = sha256(raw)
            collect(GAME, root, fetch=Mock(side_effect=AssertionError), sleep=lambda _: None)
            self.assertEqual(sha256(raw), before)

    def test_repeated_cursor_is_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                collect(GAME, Path(folder), fetch=Mock(return_value={
                    'response': {'reviews': [review()], 'cursor': '*'}}), sleep=lambda _: None)
            self.assertFalse((Path(folder) / 'raw/fixture/reviews_manifest.json').exists())

    def test_invalid_language(self):
        with self.assertRaises(ValueError):
            validate({'response': {'reviews': [review(language='french')], 'cursor': 'next'}})

    def test_terminal_page_without_reviews_is_valid(self):
        validate({
            'response': {
                'query_summary': {'num_reviews': 0},
                'cursor': 'same-cursor',
                'total_matching': 11776
            }
        })

    def test_retry_429_and_malformed(self):
        rate = Mock(status_code=429, headers={'Retry-After': '5'})
        malformed = Mock(status_code=200)
        malformed.json.return_value = {}
        good = Mock(status_code=200)
        good.json.return_value = {'response': {'reviews': []}}
        session = Mock()
        session.get.side_effect = [rate, malformed, good]
        sleep = Mock()
        get_json('https://example.test', {}, validate, session=session, sleep=sleep)
        self.assertEqual(session.get.call_count, 3)
        self.assertEqual(sleep.call_args_list[0].args[0], 5)

    def test_retry_exhaustion(self):
        session = Mock()
        session.get.side_effect = requests.Timeout()
        with self.assertRaises(RuntimeError):
            get_json('https://example.test', {}, validate, session=session, sleep=lambda _: None, attempts=2)
        self.assertEqual(session.get.call_count, 2)


if __name__ == '__main__':
    unittest.main()
