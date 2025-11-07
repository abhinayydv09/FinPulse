import feedparser
import logging
from config import FEEDS
from datetime import datetime
from html import unescape
import re

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def clean_html(raw_html):
    """Remove HTML tags and decode HTML entities."""
    clean_text = re.sub(r'<.*?>', '', raw_html)
    return unescape(clean_text.strip())

def format_published_date(entry):
    """Format the published date to a human-readable form."""
    published_raw = entry.get("published", None)
    if published_raw and hasattr(entry, "published_parsed"):
        try:
            published_dt = datetime(*entry.published_parsed[:6])
            return published_dt.strftime("%A, %d %b %Y")
        
        except Exception:
            return published_raw
    return "N/A"

def fetch_latest_feeds(limit=5):
    """Fetch the latest news entries from multiple RSS feeds."""
    all_entries = []
                                                                                                        
    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            if not feed.entries:
                logging.warning(f"No entries found for {source}.")
                continue

            entries = feed.entries[:limit]
            logging.info(f"Fetched {len(entries)} articles from {source}.")

            for e in entries:
                title = clean_html(e.get("title", "Untitled"))
                summary_text = e.get("summary", e.get("description", ""))
                summary_text = clean_html(summary_text)[:25000]

                all_entries.append({
                    "title": title,
                    "published": format_published_date(e),
                    "link": e.get("link", ""),
                    "source": source,
                    "summary_text": summary_text
                })
                                                                                                                                                                                                                                
        except Exception as ex:
            logging.error(f"Failed to parse feed from {source}: {ex}", exc_info=True)

    logging.info(f"Total entries fetched: {len(all_entries)}")
    return all_entries
                                                                                                                                                            
