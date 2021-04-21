
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import calendarific, script_logger


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        logger = script_logger.create_logger("holidays")
        calendarific.update_cache(logger=logger)
