import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHANNEL
import time

def send_telegram_message(message: str, delay: float = 1.0) -> None:
    """Send a message to Telegram channel/group."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHANNEL:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    try:
        requests.post(url, data=payload, timeout=10)
    except:
        pass
    time.sleep(delay)

