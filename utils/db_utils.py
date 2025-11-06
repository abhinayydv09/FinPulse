import sqlite3
from config import DB_PATH

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
            CREATE TABLE IF NOT EXISTS sent_feeds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT UNIQUE
            )
        """)
    conn.commit()
    conn.close()

def is_sent(link):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT 1 FROM sent_feeds WHERE link=?", (link,))
    result = c.fetchone()
    conn.close()
    return result is not None

def mark_sent(link):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO sent_feeds (link) VALUES (?)", (link,))
    conn.commit()
    conn.close()
                                                                                