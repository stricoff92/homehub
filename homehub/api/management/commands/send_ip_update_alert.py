
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import network
from api.lib import pushover


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        new_ipv4 = network.get_updated_ipv4()
        if new_ipv4 is None:
            return

        msg = f"New local IPv4 address: {new_ipv4}"
        url = f"http://{new_ipv4}{(':' + str(settings.APP_PORT)) if settings.APP_PORT else ''}"
        pushover.send_admin_alert(msg, url=url)
