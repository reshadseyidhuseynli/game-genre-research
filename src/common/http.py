import logging
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import requests


def get_json(url, params, validate, session=None, sleep=time.sleep, attempts=6):
    session = session or requests.Session()
    for attempt in range(attempts):
        delay = min(60, 2 ** (attempt + 1))
        try:
            response = session.get(url, params=params, timeout=(15, 60),
                                   headers={'User-Agent': 'game-genre-research/1.0'})
            if response.status_code == 429 or response.status_code >= 500:
                retry = response.headers.get('Retry-After')
                if retry:
                    try:
                        delay = max(delay, float(retry))
                    except ValueError:
                        delay = max(delay, (parsedate_to_datetime(retry) - datetime.now(timezone.utc)).total_seconds())
                raise ValueError(f'Transient HTTP {response.status_code}')
            response.raise_for_status()
            payload = response.json()
            validate(payload)
            return payload
        except (requests.ConnectionError, requests.Timeout, ValueError) as exc:
            if attempt == attempts - 1:
                raise RuntimeError(f'Request failed after {attempts} attempts: {url}: {exc}') from exc
            logging.warning('Request retry %s/%s in %.1fs (%s)', attempt + 1, attempts, delay, type(exc).__name__)
            sleep(delay)
