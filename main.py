import logging
from utils.fetch_feeds import fetch_latest_feeds
from utils.summarizer import summarize_text
from utils.telegram_bot import send_telegram_message
from utils.db_utils import create_table, is_sent, mark_sent


# Logging setup
# -------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s"
)


# Main process
# -------------------------------------------------------
def main():
    """
    Main entry point:
    1. Creates DB table (if not exists)
    2. Fetches latest feeds from all sources
    3. Summarizes and sends to Telegram
    4. Marks sent items in DB
    """
    logging.info("Starting FinPulse RSS Summarizer...")
    create_table()

    try:
        feeds = fetch_latest_feeds(limit=5)
        logging.info(f"Fetched {len(feeds)} total feed items.")
    except Exception as e:
        logging.error(f"Failed to fetch feeds: {e}")
        return

    for feed in feeds:
        try:
            link = feed.get("link")
            if not link:
                logging.warning("Skipping feed without link.")
                continue

            # Skip already sent links
            if is_sent(link):
                logging.info(f"Already sent: {link}")
                continue

            title = feed.get("title", "Untitled")
            published = feed.get("published", "N/A")
            source = feed.get("source", "Unknown")
            raw_summary_text = feed.get("summary_text", "")

            # Generate summary
            summary = summarize_text(raw_summary_text)

            # Format message
            message = (
                f"<b>{title}</b>\n"
                f"<i>Source:</i> {source}\n"
                f"<i>Published:</i> {published}\n\n"
                f"{summary}\n\n"
                f"<a href='{link}'>Read more</a>"
            )

            # Send to Telegram
            send_telegram_message(message)

            # Record as sent
            mark_sent(title, link, source, published, summary)
            logging.info(f"Sent & recorded: {title}")

        except Exception as e:
            logging.error(f"Error processing feed: {e}")
            continue
    
    logging.info("All new feeds processed successfully.")


# Entry point
# # --------------------------------------------------------------
if __name__ == "__main__":
    main()
