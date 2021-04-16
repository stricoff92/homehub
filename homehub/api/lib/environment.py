
from django.conf import settings


def is_testing() -> bool:
    return settings.ENV == settings.ENV_TESTING

