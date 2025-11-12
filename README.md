# FinPulse RSS Summarizer & Telegram Bot

**FinPulse** is a Python-based RSS aggregator and summarizer that fetches financial news from multiple sources, summarizes them using a HuggingFace model, and sends the summaries to a Telegram channel. It supports automated daily runs via GitHub Actions and maintains a database of already-sent feeds.

---

## Features

- Fetch latest news from multiple RSS feeds (Economic Times, MoneyControl, NDTV Profit, etc.)
- Summarize long news articles using **HuggingFace Transformer models** (`distilbart-cnn-12-6`)
- Send formatted messages directly to your **Telegram channel**
- Avoid duplicate messages by storing already-sent feeds in a SQLite database
- Fully **Dockerized** for easy deployment
- Automated daily execution using **GitHub Actions** with persistent database via artifacts

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FinPulse.git
cd FinPulse
```

### 2. Create a virtual environment (optional)
```bash
python -m venv fin
source fin/bin/activate      # Linux/macOS
fin\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
``` env
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHANNEL=@your_channel_or_chat_id
```

---

## Running Locally
```bash
python main.py
```

- The bot fetches the latest RSS feeds, summarizes them, and sends messages to your Telegram channel.
- `data/feeds.db` will be created automatically to track sent feeds.

---

## Docker Usage
### Build Docker Image
```bash
docker build -t finpulse-bot .
```

### Run Docker Container
```bash
docker run --rm \
  -e TELEGRAM_TOKEN="your_token_here" \
  -e TELEGRAM_CHANNEL="@your_channel_here" \
  -v ${PWD}:/app \
  finpulse-bot
```

- `-v ${PWD}:/app` ensures your database and logs persist locally.

---

## GitHub Actions (Automated Daily Run)
- The workflow `run_daily.yml` automatically runs the bot daily at 8 AM IST.
- Downloads the previous `feeds.db` artifact, runs the bot, and uploads the updated database.

---

## Project Structure
```
FinPulse/
│
├── main.py                 # Main bot script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── run_daily.yml           # GitHub Actions workflow
├── config.py               # Configuration (feeds, model, DB path)
├── .env                    # Environment variables
├── data/                   # SQLite database will be stored here
└── utils/                  # Helper modules
    ├── db_utils.py
    ├── fetch_feeds.py
    ├── summarizer.py
    └── telegram_bot.py
```

---

## Adding More Feeds

Edit `config.py` and update the `FEEDS` dictionary:
```python
FEEDS = {
    "Economics Times": "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
    "Money Control": "https://www.moneycontrol.com/rss/MCtopnews.xml",
    "NDTV Profit": "https://feeds.feedburner.com/ndtvprofit-latest",
}
```
---
## Notes
- **Summarization model:** By default, the bot uses `sshleifer/distilbart-cnn-12-6`.
- **Database:** `data/feeds.db` tracks sent messages to avoid duplicates.

## Author
  **Created by AY**

