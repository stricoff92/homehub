
import logging
import os.path

from django.utils import timezone
from django.conf import settings

from api.lib import environment


FILE_MODE_APPEND = "a"

def create_logger(name:str, level=logging.DEBUG, formatting="%(asctime)s - %(levelname)s - %(message)s"):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers = []
    if environment.is_testing():
        handler = logging.NullHandler()
    else:
        file_name = f"{name}-{timezone.now().strftime('%Y-%m-%d')}.log"
        file_path = os.path.join(settings.BASE_DIR, 'logs', file_name)
        handler = logging.FileHandler(file_path, mode=FILE_MODE_APPEND)
        handler.setFormatter(logging.Formatter(formatting))
    logger.addHandler(handler)
    return logger


def get_hub_logger():
    return create_logger("hub")
