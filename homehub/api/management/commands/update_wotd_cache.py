
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import wordnik, script_logger


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        logger = script_logger.create_logger("wotd")
        wordnik.update_cache(logger=logger)
