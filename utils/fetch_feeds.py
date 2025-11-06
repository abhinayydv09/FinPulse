import feedparser
from config import FEEDS
from datetime import datetime

def format_published_date(entry):
    published_raw = entry.get("published", None)
    if published_raw and hasattr(entry, "published_parsed"):
        try:
            # Convert struct_time to datetime
            published_dt = datetime(*entry.published_parsed[:6])
            # Format as "Day, DD MMM YYYY"
            return published_dt.strftime("%A, %d %b %Y")
        except Exception:
            return published_raw
    return "N/A"
                                

def fetch_latest_feeds(limit=5):
    all_entries = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        entries = feed.entries[:limit]
        for e in entries:
            all_entries.append({
                            "title": e.title,
                            "published": format_published_date(e),
                            "link": e.link,
                            "source": source,
                            "summary_text": e.get("summary", e.get("description", ""))[:1500]
                            })
    return all_entries
                