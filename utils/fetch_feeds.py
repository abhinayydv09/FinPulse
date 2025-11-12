import feedparser
from config import FEEDS
from datetime import datetime
from html import unescape
import re

def clean_html(raw_html):
    """Remove HTML tags and decode HTML entities."""
    return unescape(re.sub(r'<.*?>', '', raw_html).strip())

def format_published_date(entry):
    """Format published date to readable form."""
    published_raw = entry.get("published", None)
    if published_raw and hasattr(entry, "published_parsed"):
        try:
            dt = datetime(*entry.published_parsed[:6])
            return dt.strftime("%A, %d %b %Y")
        except:
            return published_raw
    return "N/A"

def fetch_latest_feeds(limit=5):
    """Fetch latest feeds from multiple sources."""
    all_entries = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        entries = feed.entries[:limit] if feed.entries else []
        for e in entries:
            title = clean_html(e.get("title", "Untitled"))
            summary_text = clean_html(e.get("summary", e.get("description", "")))[:1024]
            all_entries.append({
                "title": title,
                "published": format_published_date(e),
                "link": e.get("link", ""),
                "source": source,
                "summary_text": summary_text
            })
    return all_entries
