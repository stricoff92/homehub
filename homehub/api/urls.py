
from django.conf.urls import url, include
from django.urls import path

from api import views

urlpatterns = [
    path("weather", views.get_weather, name="api-get-weather"),
    path("wotd", views.get_wotd, name="api-get-wotd"),
]
