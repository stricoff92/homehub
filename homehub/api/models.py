from django.db import models


class NewsSource(models.Model):
    is_active = models.BooleanField(default=True)
    source_url = models.CharField(max_length=200)


class WeatherSource(models.Model):
    is_active = models.BooleanField(default=True)

    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
