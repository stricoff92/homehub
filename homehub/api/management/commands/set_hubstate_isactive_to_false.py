
from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import hubstate


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        hs = hubstate.HubState()
        hs.setkey(hs.STATE_KEY_IS_ONLINE, False)

