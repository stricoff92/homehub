

import json
import os.path
from typing import Dict, Set, Generator

from django.conf import settings
from django.utils import timezone
import requests

from api.models import BikeStation
from api.lib import tmp_lib, script_logger, environment


CACHE_FILE_NAME = "bikes.json"
if environment.is_testing():
    CACHE_FILE_NAME = "test-" + CACHE_FILE_NAME


class BikesCacheIsEmptyError(Exception):
    pass


def fetch_json(network:str, stations:Set[str]) -> Generator:
    url = f"http://api.citybik.es/v2/networks/{network}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    for station in data['network']['stations']:
        if station['id'] in stations:
            yield station


def update_cache(logger=None) -> None:
    logger = logger or script_logger.create_logger("bikes")
    logger.info(f"(updating cache) -> Fetching data from http://api.citybik.es/v2/networks/")

    stations = BikeStation.objects.filter(is_active=True)
    target_network = stations.first().network
    target_stations = set(stations.values_list("station_id", flat=True))

    try:
        stations_data = list(fetch_json(target_network, target_stations))
    except Exception as e:
        logger.error(f"could not fetch data {e}")
        raise

    logger.info(f"data fetched for {len(stations_data)} stations")

    station_name_map = dict(stations.values_list('station_id', 'name'))
    for ix, station in enumerate(stations_data):
        stations_data[ix]['name'] = station_name_map[station['id']]
        logger.debug(f"found data for station {station_name_map[station['id']]}")

    data_to_cache = {
        'data':stations_data,
        'updated_at':timezone.now().isoformat()
    }

    file_name = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    logger.info(f"updating tmp file {file_name}")
    with open(file_name, "w") as f:
        json.dump(data_to_cache, f)


def read_cache() -> Dict:
    file_path = tmp_lib.generate_named_tmp_file(CACHE_FILE_NAME)
    if not os.path.exists(file_path):
        raise BikesCacheIsEmptyError()
    with open(file_path, "r") as f:
        return json.load(f)
