from django.contrib import admin

from api.models import (
    NewsSource,
    WeatherSource,
    BikeStation,
)

# Register your models here.

admin.site.register(NewsSource)
admin.site.register(WeatherSource)
admin.site.register(BikeStation)
