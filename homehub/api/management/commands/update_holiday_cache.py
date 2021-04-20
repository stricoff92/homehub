
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import calendarific


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        calendarific.update_cache()
