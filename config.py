import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

# Telegram bot token and channel
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")

# RSS feeds
FEEDS = {
    "Economics Times": "https://economictimes.indiatimes.com/rssfeedstopstories.cms",
    "Money Control": "https://www.moneycontrol.com/rss/MCtopnews.xml",
    "NDTV Profit": "https://feeds.feedburner.com/NdtvProfit-TopNews"
    }

# Summarization parameters
SUMMARY_PARAMS = {
    "max_length": 100,
    "min_length": 30,
    "length_penalty": 1.0,
    "num_beams": 6,
    "early_stopping" : True
    }

# Database path
DB_PATH = "feeds.db"
