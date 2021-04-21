
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import vulnerability, script_logger


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        logger = script_logger.create_logger("vulnerabilities")
        vulnerability.refresh_db_data(logger=logger)
