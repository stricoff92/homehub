
from django.conf.urls import url, include
from django.urls import path

from website import views

urlpatterns = [
    path("", views.landing, name="app-landing")
]
