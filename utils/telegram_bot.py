import logging
import requests
import time
from config import TELEGRAM_TOKEN, TELEGRAM_CHANNEL


# Logging Setup
# -------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s"
)


# Send Message to Telegram
# -------------------------------------------------------
def send_telegram_message(message: str, delay: float = 1.0) -> None:
    """
    Sends a formatted message to a Telegram channel or group.
    Args:
        message (str): The message content (HTML formatted)
        delay (float): Optional delay between messages to prevent flooding
    """
    if not TELEGRAM_TOKEN or not TELEGRAM_CHANNEL:
        logging.error("Telegram configuration missing in .env or config.py")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False 
        }
    
    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code == 200:
            logging.info("Message sent successfully to Telegram channel.")
        else:                                
            logging.error(f"Failed to send message: {response.text}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Telegram API request failed: {e}")

    # Delay to prevent hitting Telegram rate limits when sending multiple messages
    time.sleep(delay)
                                                                                                                                        
