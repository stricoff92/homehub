

from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import bikes


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bikes.update_cache()

