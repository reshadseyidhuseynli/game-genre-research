import logging


def setup():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def run_cli(action):
    setup()
    try:
        action()
    except Exception as exc:
        logging.error('%s', exc)
        raise SystemExit(1) from exc
