
import os

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # This is pretty janky, ok it's very janky...
        os.system("nohup sleep 2 && reboot > /dev/null & disown")
