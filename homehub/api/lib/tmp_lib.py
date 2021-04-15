
import os.path
import uuid

from django.conf import settings


def generate_new_tmp_file_name(ext="txt") -> str:
    while True:
        uid = uuid.uuid4().hex
        file_name = os.path.join(settings.BASE_DIR, "tmp", f"{uid}.{ext}")
        if not os.path.exists(file_name):
            return file_name


def generate_named_tmp_file(filename) -> str:
    return os.path.join(settings.BASE_DIR, "tmp", filename)
