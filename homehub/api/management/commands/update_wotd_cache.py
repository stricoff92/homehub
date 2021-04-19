
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import wordnik


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        wordnik.update_cache()
