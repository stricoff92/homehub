

import json
import hashlib
import os.path
from typing import Dict

from django.conf import settings
import requests

from api.models import WeatherSource
from api.lib import tmp_lib, script_logger, environment

API_BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"
CACHE_FILE_NAME = "weather.json"
if environment.is_testing():
    CACHE_FILE_NAME = 'test-' + CACHE_FILE_NAME


class NoActiveWeatherSourcesError(Exception):
    pass

class WeatherCacheIsEmptyError(Exception):
    pass


def fetch_json() -> Dict:
    weather_source = WeatherSource.objects.filter(is_active=True).first()
    if not weather_source:
        raise NoActiveWeatherSourcesError()

    data = {
        'lat':weather_source.latitude,
        'lon':weather_source.longitude,
        'appid':settings.WEATHER_API_KEY,
        'exclude':'minutely',
    }

    response = requests.get(API_BASE_URL, params=data)
    response.raise_for_status()
    return response.json()


def hash_weather_dict(data:Dict) -> str:
    return hashlib.md5(json.dumps(data).encode()).hexdigest()


def update_cache() -> None:
    logger = script_logger.get_hub_logger()
    logger.info(f"(updating cache) -> Fetching data from {API_BASE_URL}")
    try:
        data = fetch_json()
    except Exception as e:
        logger.error(f"Failed to fetch data: {e}")
        raise

    data_hash = hash_weather_dict(data)
    data['hash'] = data_hash
    logger.info(f"data fetched, hash:{data_hash}")

    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    with open(file_path, "w") as f:
        json.dump(data, f)


def read_cache() -> Dict:
    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    if not os.path.exists(file_path):
        raise WeatherCacheIsEmptyError()
    with open(file_path, "r") as f:
        return json.load(f)


def delete_cache() -> None:
    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    if os.path.exists(file_path):
        os.remove(file_path)
