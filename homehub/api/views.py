
import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.lib import openweather, wordnik


@api_view(['GET'])
@permission_classes([])
def get_weather(request):
    try:
        weather_data = openweather.read_cache()
    except openweather.WeatherCacheIsEmptyError:
        return Response("No Weather Found", status.HTTP_404_NOT_FOUND)

    return Response(weather_data, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def get_wotd(request):
    try:
        weather_data = wordnik.read_cache()
    except wordnik.WOTDCacheIsEmptyError:
        return Response("No word of the day found", status.HTTP_404_NOT_FOUND)

    return Response(weather_data, status.HTTP_200_OK)
