
import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.lib import openweather


@api_view(['GET'])
@permission_classes([])
def get_weather(request):
    try:
        weather_data = openweather.read_cache()
    except WeatherCacheIsEmptyError:
        return Response("No Weather Found", status.HTTP_404_NOT_FOUND)

    return Response(weather_data, status.HTTP_200_OK)

