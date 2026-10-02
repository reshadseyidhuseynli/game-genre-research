import logging
from src.common.config import arguments, load_game
from src.common.logging import run_cli
from src.collectors.steam_metadata import collect as metadata
from src.collectors.steam_reviews import collect as reviews
from src.processors.clean_reviews import process
from src.reports.game_report import generate as report
from src.verify import verify


def main():
    parser = arguments('Collect, process, calculate statistics and report')
    parser.add_argument('--offline', action='store_true', help='Rebuild from existing complete raw snapshot')
    args = parser.parse_args()
    game = load_game(args.game, args.config)
    steps = [] if args.offline else [('metadata collection', metadata), ('review collection', reviews)]
    steps += [('processing', process), ('statistics and report', report), ('verification', verify)]
    for name, function in steps:
        logging.info('%s: %s', game['name'], name)
        try:
            function(game, args.data_dir)
        except Exception as exc:
            raise RuntimeError(f'{name} failed: {exc}') from exc


if __name__ == '__main__':
    run_cli(main)
