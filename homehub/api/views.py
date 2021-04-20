
import json

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.lib import openweather, wordnik, bikes, vulnerability, calendarific


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


@api_view(['GET'])
@permission_classes([])
def get_bikes(request):
    try:
        bikes_data = bikes.read_cache()
    except bikes.BikesCacheIsEmptyError:
        return Response("No bike data found", status.HTTP_404_NOT_FOUND)

    return Response(bikes_data, status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([])
def get_vulnerability(request):
    try:
        v = vulnerability.select_random_vulnerability_item()
    except vulnerability.NoVulnernabilitiesError:
        return Response("No Vulneravility data found", status.HTTP_404_NOT_FOUND)

    v.displayed_at = timezone.now()
    v.displayed_once = True
    v.save(update_fields=["displayed_at", "displayed_once"])

    data = {
        'cve_identifier':v.cve_identifier,
        'description':v.description,
    }
    return Response(data, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def get_next_holidays(request):
    try:
        holidays = list(calendarific.read_upcoming_holidays(4))
    except calendarific.HolidayCacheIsEmptyError:
        return Response("No holiday data found", status.HTTP_404_NOT_FOUND)

    return Response(holidays, status.HTTP_200_OK)
