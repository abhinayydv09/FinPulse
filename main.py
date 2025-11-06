from utils.fetch_feeds import fetch_latest_feeds
from utils.summarizer import summarize_text
from utils.telegram_bot import send_telegram_message
from utils.db_utils import create_table, is_sent, mark_sent

def main():
    create_table()
    feeds = fetch_latest_feeds()
    for feed in feeds:
        if not is_sent(feed["link"]):

            title = feed["title"]
            link = feed["link"]
            published = feed["published"]
            source = feed["source"]

            # Summarize the article
            summary = summarize_text(feed["summary"])

            # Format the message for Telegram
            message = (
                        f"<b>{title}</b>\n"
                        f"<i>Source:</i> {source}\n"
                        f"<i>Published:</i> {published}\n\n"
                        f"{summary}\n\n"
                        f"<a href='{link}'>Read more</a>"
                    )

            # Send to Telegram channel
            send_telegram_message(message)
            mark_sent(feed["link"])

if __name__ == "__main__":
    main()
