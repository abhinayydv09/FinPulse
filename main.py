from utils.fetch_feeds import fetch_latest_feeds
from utils.summarizer import summarize_text
from utils.telegram_bot import send_telegram_message
from utils.db_utils import init_db, is_sent, mark_sent

def main():
    init_db()
    feeds = fetch_latest_feeds()
    for feed in feeds:
        if not is_sent(feed["link"]):
            summary = summarize_text(feed["title"])
            message = f"<b>Title:</b> {feed['title']}\n" \
                      f"<b>Source:</b> {feed['source']}\n" \
                      f"<b>Published:</b> {feed['published']}\n" \
                      f"<b>Summary:</b> {summary}\n" \
                      f"<b>Link:</b> {feed['link']}"
            send_telegram_message(message)
            mark_sent(feed["link"])

if __name__ == "__main__":
    main()
