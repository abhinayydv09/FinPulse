import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from utils.fetch_feeds import fetch_latest_feeds
from utils.summarizer import summarize_text
from utils.telegram_bot import send_telegram_message
from utils.db_utils import create_table, is_sent, mark_sent
import logging
import warnings

warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)



def main():
    
    create_table()
    
    feeds = fetch_latest_feeds(limit=5)

    for feed in feeds:
        
        link = feed.get("link")
        if not link or is_sent(link):
            continue

        title = feed.get("title", "Untitled")
        published = feed.get("published", "N/A")
        source = feed.get("source", "Unknown")
        raw_summary_text = feed.get("summary_text", "")
        summary = summarize_text(raw_summary_text)

        message = (
            f"<b>{title}</b>\n"
            f"<i>{source} • {published}</i>\n\n"
            f"{summary}\n"
            f"<a href='{link}'><i>Read more</i></a>"
        )

        send_telegram_message(message)
        mark_sent(title, link, source, published, summary)

if __name__ == "__main__":
    main()
