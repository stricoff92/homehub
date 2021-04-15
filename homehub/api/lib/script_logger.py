
import logging
import os.path

from django.utils import timezone
from django.conf import settings

from api.lib import environment


def create_logger(name:str, level=logging.DEBUG, formatting="%(asctime)s - %(levelname)s - %(message)s"):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if environment.is_testing():
        handler = logging.NullHandler()
    else:
        file_name = f"{name}-{timezone.now().strftime('%Y-%m-%d%_H%M%S')}.log"
        file_path = os.path.join(settings.BASE_DIR, 'logs', file_name)
        handler = logging.FileHandler(file_path)
        handler.setFormatter(logging.Formatter(formatting))
    logger.addHandler(handler)
    return logger


def get_hub_logger():
    return create_logger("hub")
