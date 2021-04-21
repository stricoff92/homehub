
from django.conf import settings
import requests

def send_admin_alert(message:str, **data) -> str:
    if not settings.PUSHOVER_APP_TOKEN:
        return
    data = {
        "token": settings.PUSHOVER_APP_TOKEN,
        "user": settings.PUSHOVER_USER_TOKEN,
        "message": message,
        **data
    }
    url = "https://api.pushover.net:443/1/messages.json"
    response = requests.post(url, timeout=4, data=data)
    response.raise_for_status()
