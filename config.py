import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")  # e.g. @your_channel or numeric chat_id

# RSS feeds (defaults; you can override via .env or edit here)
FEEDS = {
    "Economics Times": os.getenv("FEED_ECONOMICTIMES", "https://economictimes.indiatimes.com/rssfeedstopstories.cms"),
    "Money Control": os.getenv("FEED_MONEYCONTROL", "https://www.moneycontrol.com/rss/MCtopnews.xml"),
    "NDTV Profit": os.getenv("FEED_NDTV", "https://feeds.feedburner.com/NdtvProfit-TopNews"),
}

# Summarizer parameters
SUMMARY_PARAMS = {
    "max_length": int(os.getenv("SUM_MAX_LENGTH", 100)),
    "min_length": int(os.getenv("SUM_MIN_LENGTH", 30)),
    "length_penalty": float(os.getenv("SUM_LENGTH_PENALTY", 1.0)),
    "num_beams": int(os.getenv("SUM_NUM_BEAMS", 6)),
    "early_stopping": os.getenv("SUM_EARLY_STOPPING", "True").lower() in ("1", "true", "yes"),
}

# Model
MODEL_NAME = os.getenv("MODEL_NAME", "sshleifer/distilbart-cnn-12-6")

# DB
DB_PATH = os.getenv("DB_PATH", "feeds.db")
