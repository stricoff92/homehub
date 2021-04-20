

from django.core.management.base import BaseCommand
from django.conf import settings

from api.lib import bikes, hubstate, script_logger


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        logger = script_logger.get_hub_logger()
        hs = hubstate.HubState()
        if not hs.getkey(hs.STATE_KEY_IS_ONLINE):
            logger.debug("skipping bikes update")
            return

        bikes.update_cache()

