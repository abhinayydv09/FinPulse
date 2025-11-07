import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")  # e.g. @your_channel or numeric chat_id

# RSS feeds (defaults; you can override via .env or edit here)
FEEDS = {
    "Economics Times": "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
    "Money Control": "https://www.moneycontrol.com/rss/MCtopnews.xml",
    "NDTV Profit": "https://feeds.feedburner.com/ndtvprofit-latest",
}

# Summarizer parameters
SUMMARY_PARAMS = {
    "max_length": 100,
    "min_length": 30,
    "length_penalty": 1.0,
    "num_beams": 6,
    "early_stopping": "True".lower() in ("1", "true", "yes"),
}

# Model
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

# DB
DB_PATH = os.path.join(os.getcwd(), "feeds.db")
