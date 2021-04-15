from django.db import models


class NewsSource(models.Model):
    is_active = models.BooleanField(default=True)
    source_url = models.CharField(max_length=200)


class WeatherSource(models.Model):
    is_active = models.BooleanField(default=True)

    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"<WS{self.pk} {self.name} {self.latitude} {self.longitude}>"
