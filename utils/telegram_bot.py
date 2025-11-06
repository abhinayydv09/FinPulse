import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHANNEL

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
                "chat_id": TELEGRAM_CHANNEL,
                "text": message,
                "parse_mode": "HTML"
               }
    response = requests.post(url, data=payload)
    
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
    else:
        print("Message sent successfully.")
                