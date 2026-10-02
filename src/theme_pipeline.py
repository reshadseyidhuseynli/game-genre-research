import logging

from src.common.config import arguments, load_game
from src.common.logging import run_cli
from src.processors.theme_candidates import generate as generate_candidates
from src.reports.theme_candidate_report import generate as generate_report


def main():
    args = arguments('Run deterministic theme candidate analysis and report').parse_args()
    game = load_game(args.game, args.config)

    logging.info('%s: theme candidate scan', game['name'])
    generate_candidates(game, args.data_dir)

    logging.info('%s: theme candidate report', game['name'])
    path = generate_report(game, args.data_dir)
    logging.info('Theme candidate report written: %s', path)


if __name__ == '__main__':
    run_cli(main)
