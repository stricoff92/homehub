
from django.conf.urls import url, include
from django.urls import path

from api import views

urlpatterns = [
    path("weather", views.get_weather, name="api-get-weather"),
    path("wotd", views.get_wotd, name="api-get-wotd"),
    path("bikes", views.get_bikes, name="api-get-bikes"),
    path("vulnerability", views.get_vulnerability, name="api-get-vulnerability"),
    path("holidays", views.get_next_holidays, name="api-get-holidays"),
]
