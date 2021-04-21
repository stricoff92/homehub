
import datetime as dt
import json
import hashlib
import os.path
from typing import Dict, Generator

from django.conf import settings
import requests

from api.models import WeatherSource
from api.lib import tmp_lib, script_logger, environment


CACHE_FILE_NAME = "holidays.json"
if environment.is_testing():
    CACHE_FILE_NAME = 'test-' + CACHE_FILE_NAME


class HolidayCacheIsEmptyError(Exception):
    pass


def get_api_url(year:int, country_code="US") -> str:
    return f"https://calendarific.com/api/v2/holidays?api_key={settings.CALENDARIFIC_API_KEY}&country={country_code}&year={year}"


def fetch_json(year:int):
    response = requests.get(get_api_url(year))
    response.raise_for_status()
    return response.json()


def update_cache(year=None, logger=None) -> None:
    logger = logger or script_logger.create_logger("holidays")
    year = year or dt.datetime.now().year
    logger.info(f"(updating cache) -> Fetching holiday data for year {year}")

    try:
        data = fetch_json(year)['response']['holidays']
    except Exception as e:
        logger.error(f"could not fetch data {e}")
        raise

    data.sort(
        key=lambda h: dt.datetime.strptime(h['date']['iso'].split('T')[0], '%Y-%m-%d').date())

    logger.info(f"(updating cache) -> Fetched {len(data)} holidays")

    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    with open(file_path, "w") as f:
        json.dump(data, f)


def read_cache() -> Dict:
    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    if not os.path.exists(file_path):
        raise HolidayCacheIsEmptyError()
    with open(file_path, "r") as f:
        return json.load(f)


def read_upcoming_holidays(count:int) -> Generator:
    today = dt.date.today()
    holidays = read_cache()

    returned_holidays = 0
    for holiday in holidays:
        holiday_date = dt.datetime.strptime(holiday['date']['iso'].split('T')[0], '%Y-%m-%d').date()

        if holiday_date < today:
            continue
        else:
            yield holiday
            returned_holidays += 1
            if returned_holidays >= count:
                break
