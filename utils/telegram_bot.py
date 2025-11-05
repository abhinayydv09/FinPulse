import requests
from utils.config import TELEGRAM_TOKEN, TELEGRAM_CHANNEL

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
                "chat_id": TELEGRAM_CHANNEL,
                "text": message,
                "parse_mode": "HTML"
               }
    requests.post(url, data=payload)
    