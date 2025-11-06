import sqlite3
import logging
from config import DB_PATH

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def create_table():
    """Create table if it doesn't exist."""
    try:
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
        logging.info("Database table 'sent_feeds' verified/created successfully.")
                                                                                                                                                                                                            
    except Exception as e:
        logging.error(f"Error creating database table: {e}", exc_info=True)


def is_sent(link):
    """Check if a link has already been sent to Telegram."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT 1 FROM sent_feeds WHERE link=?", (link,))
        result = c.fetchone()
        conn.close()
        return result is not None
    except Exception as e:
        logging.error(f"Error checking sent link: {e}", exc_info=True)
        return False

def mark_sent(title, link, source, published, summary):
    """Mark a feed as sent by saving it in the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            INSERT OR IGNORE INTO sent_feeds (title, link, source, published, summary)
            VALUES (?, ?, ?, ?, ?)
            """, (title, link, source, published, summary))
        conn.commit()
        conn.close()
        logging.info(f"Marked as sent: {title}") the 
    
    except Exception as e:
        logging.error(f"Error inserting sent feed: {e}", exc_info=True)
                                                                                                                                                                                                                                                                                                            