import logging
from datetime import datetime, timezone
from src.common.config import arguments, load_game
from src.common.http import get_json
from src.common.io import read_json, write_json
from src.common.logging import run_cli

ENDPOINT = 'https://store.steampowered.com/api/appdetails'


def normalize_metadata(payload, game):
    data = payload[str(game['steam_app_id'])]['data']
    price = data.get('price_overview') or {}
    fields = ('name', 'release_date', 'developers', 'publishers', 'is_free',
              'short_description', 'genres', 'categories', 'supported_languages', 'header_image')
    return {**{k: data.get(k) for k in fields}, 'steam_app_id': game['steam_app_id'],
            'price': price.get('final'), 'currency': price.get('currency'),
            'price_unit': 'minor currency units',
            'store_url': f"https://store.steampowered.com/app/{game['steam_app_id']}/"}


def collect(game, data_dir):
    path = data_dir / 'raw' / game['key'] / 'steam_metadata.json'
    if path.exists():
        logging.info('Using immutable metadata snapshot')
        snapshot = read_json(path)
        if snapshot['params']['appids'] != game['steam_app_id']:
            raise ValueError('Metadata snapshot does not match configured app')
        return snapshot
    params = {'appids': game['steam_app_id'], 'l': 'english', 'cc': 'us'}
    def validate(payload):
        item = payload.get(str(game['steam_app_id']), {})
        if item.get('success') is not True or not isinstance(item.get('data'), dict):
            raise ValueError('Metadata response missing successful app data')
    payload = get_json(ENDPOINT, params, validate)
    snapshot = {'endpoint': ENDPOINT, 'params': params,
                'collected_at': datetime.now(timezone.utc).isoformat(), 'response': payload}
    write_json(path, snapshot, immutable=True)
    return snapshot


def main():
    args = arguments('Collect Steam metadata').parse_args()
    collect(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
