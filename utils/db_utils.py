import sqlite3
from config import DB_PATH, DATA_DIR
import os

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def create_table():
    """Create the sent_feeds table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sent_feeds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT UNIQUE,
            source TEXT,
            published TEXT,
            summary TEXT
        )
    """)
    conn.commit()
    conn.close()

def is_sent(link):
    """Check if a link has already been sent."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT 1 FROM sent_feeds WHERE link=?", (link,))
    result = c.fetchone()
    conn.close()
    return result is not None

def mark_sent(title, link, source, published, summary):
    """Mark a feed as sent."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO sent_feeds (title, link, source, published, summary)
        VALUES (?, ?, ?, ?, ?)
    """, (title, link, source, published, summary))
    conn.commit()
    conn.close()
