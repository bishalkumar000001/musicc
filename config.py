# Configuration file for Telegram Music Bot
import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_NAME = "JunoXmusic"
BOT_USERNAME = "Junomusic_bot"
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ASSISTANT_ACCOUNT = os.getenv("ASSISTANT_ACCOUNT", "")

# Database Configuration
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "music_bot")

# Admin Configuration
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split())) if os.getenv("ADMIN_IDS") else []
OWNER_ID = int(os.getenv("OWNER_ID", 0))
LOGGER_CHANNEL_ID = int(os.getenv("LOGGER_CHANNEL_ID", 0)) if os.getenv("LOGGER_CHANNEL_ID") else None

# Music Configuration
MAX_QUEUE_SIZE = 100
CACHE_DIR = "downloads"
LOG_DIR = "logs"

# Ensure directories exist
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
