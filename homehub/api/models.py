from django.db import models


class NewsSource(models.Model):
    is_active = models.BooleanField(default=True)
    source_url = models.CharField(max_length=200)

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"<NS{self.pk} {self.name}>"


class WeatherSource(models.Model):
    is_active = models.BooleanField(default=True)

    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"<WS{self.pk} {self.name} {self.latitude} {self.longitude}>"


class BikeStation(models.Model):
    is_active = models.BooleanField(default=True)

    name = models.CharField(max_length=30)
    network = models.CharField(max_length=40)
    station_id = models.CharField(max_length=100)


    def __str__(self) -> str:
        return f"<BS{self.pk} {self.name} ({self.network})>"
