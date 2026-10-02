import argparse
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_game(key, path=ROOT / 'config/games.yaml'):
    with Path(path).open(encoding='utf-8') as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict) or not isinstance(config.get('games'), list):
        raise ValueError('Config requires a games list')
    keys = set()
    for game in config['games']:
        if not re.fullmatch(r'[a-z0-9_-]+', game.get('key', '')):
            raise ValueError('Invalid game key')
        if game['key'] in keys:
            raise ValueError('Duplicate game key')
        keys.add(game['key'])
        if type(game.get('steam_app_id')) is not int or game['steam_app_id'] <= 0:
            raise ValueError('steam_app_id must be a positive integer')
        if not isinstance(game.get('name'), str) or not game['name'].strip():
            raise ValueError('Game name is required')
    size = config.get('sample_size', 50)
    delay = config.get('request_delay_seconds', 2)
    if type(size) is not int or size <= 0 or not isinstance(delay, (int, float)) or delay < 1:
        raise ValueError('Invalid sample size or request delay (minimum 1 second)')
    for game in config['games']:
        if game['key'] == key:
            return {**game, 'sample_size': size, 'request_delay_seconds': delay}
    raise ValueError(f'Unknown game: {key}')


def arguments(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--game', required=True)
    parser.add_argument('--config', type=Path, default=ROOT / 'config/games.yaml')
    parser.add_argument('--data-dir', type=Path, default=ROOT / 'data')
    return parser
