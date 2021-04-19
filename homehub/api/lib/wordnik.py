
import json
import os.path
from typing import Dict

from django.conf import settings
import requests

from api.lib import tmp_lib, script_logger, environment


WORD_OF_THE_DAY_API_URL = "https://api.wordnik.com/v4/words.json/wordOfTheDay"
CACHE_FILE_NAME = "wotd.json"
if environment.is_testing():
    CACHE_FILE_NAME = 'test-' + CACHE_FILE_NAME


class WOTDCacheIsEmptyError(Exception):
    pass


def fetch_json() -> Dict:
    url = WORD_OF_THE_DAY_API_URL
    params = {
        'api_key':settings.WORDNIK_API_KEY
    }
    headers = {
        'Accept':'application/json'
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def update_cache() -> None:
    logger = script_logger.get_hub_logger()
    logger.info(f"(updating cache) -> Fetching data from {WORD_OF_THE_DAY_API_URL}")
    try:
        data = fetch_json()
    except Exception as e:
        logger.error(f"Failed to fetch data: {e}")
        raise

    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    with open(file_path, "w") as f:
        json.dump(data, f)


def read_cache() -> Dict:
    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    if not os.path.exists(file_path):
        raise WOTDCacheIsEmptyError()
    with open(file_path, "r") as f:
        return json.load(f)

