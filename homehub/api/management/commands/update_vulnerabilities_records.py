
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import vulnerability


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vulnerability.refresh_db_data()
