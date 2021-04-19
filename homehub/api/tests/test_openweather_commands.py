
import os.path
from unittest.mock import patch

from django.test import TestCase
from django.core.management import call_command
from django.conf import settings
from rest_framework import status
import requests

from api.lib import hubstate, openweather
from api.models import WeatherSource


class HubStateTestCases(TestCase):
    def setUp(self):
        super().setUp()
        self.mock_get = patch.object(requests, "get").start()
        self.hs = hubstate.HubState()

        self.weather_source = WeatherSource.objects.create(
            longitude="50.0000", latitude="75.0000", is_active=True, name="foobar")
        self.assertEqual(WeatherSource.objects.count(), 1)


    def tearDown(self):
        self.mock_get.stop()
        self.hs.delete_file()
        super().tearDown()


    def test_no_calls_are_made_when_hubstate_is_offline(self):
        """ Test that the cronjob does nothing when hubstate is set to false
        """
        self.hs.setkey(self.hs.STATE_KEY_IS_ONLINE, False)
        call_command("update_weather_cache")
        self.mock_get.assert_not_called()


    def test_weather_cache_is_updated_when_hubstate_is_online(self):
        self.hs.setkey(self.hs.STATE_KEY_IS_ONLINE, True)

        class MockHTTPResponse:
            def __init__(self):
                self.status = status.HTTP_200_OK
            def raise_for_status(self):
                pass
            def json(self):
                return {"hello": "world!"}

        self.mock_get.return_value = MockHTTPResponse()

        call_command("update_weather_cache")
        self.mock_get.assert_called_once_with(
            openweather.API_BASE_URL, params={
            'lat':self.weather_source.latitude,
            'lon':self.weather_source.longitude,
            'appid':settings.WEATHER_API_KEY,
            'exclude':'minutely',
        })

        data_in_cache = openweather.read_cache()
        self.assertEqual(
            data_in_cache,
            {'hello': 'world!', 'hash': '3f87dedbef528f7dfb7243c6db0917c3', 'weather_location_name': 'foobar'}
        )
