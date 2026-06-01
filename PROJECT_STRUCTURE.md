# 📁 Project Structure

Detailed explanation of all files and directories in the Music Bot project.

## Directory Overview

```
musicc/
├── bot.py                    # Main bot application
├── config.py                 # Configuration settings
├── database.py               # MongoDB operations
├── music_handler.py          # Music download/search
├── helpers.py                # Helper functions and filters
├── advanced_commands.py      # Advanced bot features
├── logger_config.py          # Logging configuration
├── test_config.py            # Configuration testing
│
├── requirements.txt          # Python dependencies
├── requirements-dev.txt      # Development dependencies
│
├── Dockerfile                # Docker image definition
├── docker-compose.yml        # Docker compose config
├── Makefile                  # Convenient commands
│
├── .env.example              # Environment template
├── .gitignore                # Git ignore file
│
├── README.md                 # Main documentation
├── INSTALLATION.md           # Installation guide
├── QUICK_START.md            # Quick setup guide
├── COMMANDS.md               # Command reference
├── LICENSE                   # MIT License
│
├── downloads/                # Cache for downloaded music
├── logs/                     # Bot log files
└── .git/                     # Git repository
```

## Core Files Explanation

### 🤖 `bot.py` (Main Application)
- **Purpose:** Main bot application with command handlers
- **Size:** ~600 lines
- **Functions:**
  - Command handlers for all user commands
  - Admin command handlers
  - Owner command handlers
  - Callback query handlers for inline buttons
  - Main bot initialization and startup

**Key Commands:**
- `/start`, `/help`, `/play`, `/search`
- `/queue`, `/current`, `/skip`, `/pause`
- `/resume`, `/stop`, `/stats`, `/ping`
- Admin and owner specific commands

---

### ⚙️ `config.py` (Configuration)
- **Purpose:** Centralized configuration management
- **Loads from:** `.env` file via environment variables
- **Provides:**
  - Telegram API credentials (API_ID, API_HASH, BOT_TOKEN)
  - Database configuration (MongoDB URI, DB name)
  - Admin and owner IDs
  - Music bot settings (queue size, cache directory)
  - Directory creation and validation

**Configuration Variables:**
```python
API_ID              # Telegram API ID
API_HASH            # Telegram API Hash
BOT_TOKEN           # Bot token from @BotFather
MONGO_DB_URI        # MongoDB connection string
DB_NAME             # Database name
ADMIN_IDS           # List of admin IDs
OWNER_ID            # Bot owner ID
MAX_QUEUE_SIZE      # Maximum songs in queue
CACHE_DIR           # Download cache directory
LOG_DIR             # Log file directory
```

---

### 💾 `database.py` (Database Operations)
- **Purpose:** MongoDB operations and data management
- **Database:** MongoDB with Collections for Users, Queue, Admins
- **Class:** `Database` with static methods

**Collections:**
1. **users** - User profiles and statistics
   - user_id, username, last_seen, commands_used

2. **queue** - Song queue per chat
   - chat_id, url, title, added_by, added_at

3. **admins** - Admin privileges per chat
   - user_id, chat_id, added_at

**Methods:**
```python
add_user(user_id, username)
add_to_queue(chat_id, song_url, song_title, added_by)
get_queue(chat_id)
remove_from_queue(chat_id, song_id)
clear_queue(chat_id)
add_admin(user_id, chat_id)
remove_admin(user_id, chat_id)
is_admin(user_id, chat_id)
get_chat_admins(chat_id)
```

---

### 🎵 `music_handler.py` (Music Operations)
- **Purpose:** Handle music download, search, and management
- **Library:** yt-dlp for YouTube downloads
- **Class:** `MusicHandler` with static methods

**Methods:**
```python
download_audio(url)          # Download from URL
search_song(query)           # Search YouTube
get_file_path(title)         # Get downloaded file path
delete_audio(file_path)      # Delete cached file
get_duration(file_path)      # Get audio duration
```

**Returns:** Song info with title, duration, uploader, thumbnail

---

### 🛠️ `helpers.py` (Helper Functions)
- **Purpose:** Shared utilities for the bot
- **Classes:**
  - `Filters` - Authorization checks
  - `Utils` - Formatting and utility functions
  - `MessageBuilder` - Build formatted messages

**Filters:**
- `is_admin()` - Check admin status
- `is_owner()` - Check owner status
- `is_group()` - Check if group chat

**Utils:**
- `format_duration()` - Convert seconds to MM:SS
- `truncate_text()` - Limit text length

**MessageBuilder:**
- `build_help_message()` - Help text with all commands
- `build_queue_message()` - Formatted queue display

---

### 🚀 `advanced_commands.py` (Advanced Features)
- **Purpose:** Advanced commands and features
- **Classes:**
  - `AdvancedMusicCommands` - DJ mode, loops, EQ
  - `BotStatistics` - Bot statistics
  - `NotificationSystem` - User notifications

**Features:**
- Playlist management
- Favorites system
- Music recommendations
- Song lyrics display
- DJ mode
- Loop modes (off, one, all)
- Shuffle
- Equalizer presets
- Custom radio stations

---

### 📝 `logger_config.py` (Logging)
- **Purpose:** Configure logging for the bot
- **Features:**
  - Rotating file handler (10MB per file, 10 backups)
  - Console output
  - Timestamped logs
  - Formatted messages

**Log Location:** `logs/bot.log`

---

### 🧪 `test_config.py` (Configuration Testing)
- **Purpose:** Validate bot configuration before startup
- **Checks:**
  - .env file exists
  - All credentials set
  - FFmpeg installed
  - MongoDB accessible
  - Python packages installed
  - Directories exist

**Usage:** `python test_config.py`

---

## Configuration Files

### 📄 `.env.example` (Environment Template)
```bash
API_ID=0                                    # Your API ID
API_HASH=your_api_hash                     # Your API Hash
BOT_TOKEN=your_bot_token                   # Bot token
ASSISTANT_ACCOUNT=@assistant_username      # Optional
MONGO_DB_URI=mongodb://localhost:27017
DB_NAME=music_bot
OWNER_ID=your_user_id
ADMIN_IDS=admin_id_1 admin_id_2 admin_id_3
```

### 📦 `requirements.txt` (Dependencies)
```
pyrogram==1.4.16          # Telegram Bot Framework
TgCrypto==1.2.5           # Telegram Encryption
python-dotenv==0.21.0     # Environment variables
yt-dlp==2023.12.30        # YouTube downloader
pydub==0.25.1             # Audio processing
requests==2.31.0          # HTTP library
pymongo==4.6.0            # MongoDB driver
```

### 📦 `requirements-dev.txt` (Development)
```
pytest==7.4.3             # Testing framework
pytest-asyncio==0.21.1    # Async test support
black==23.12.0            # Code formatter
flake8==6.1.0             # Code linter
pylint==3.0.3             # Code analyzer
isort==5.13.2             # Import sorter
```

---

## Docker Files

### 🐳 `Dockerfile`
- **Base Image:** `python:3.9-slim`
- **Setup:**
  - Installs FFmpeg and system dependencies
  - Installs Python packages
  - Creates working directory
  - Sets environment variables
- **Command:** Runs `python bot.py`

### 🐳 `docker-compose.yml`
- **Services:**
  - `mongodb` - MongoDB database
  - `music_bot` - Bot application
- **Volumes:**
  - MongoDB data persistence
  - Bot downloads and logs
  - .env file mounting
- **Networks:** Custom bridge network
- **Restart:** Always enabled

---

## Documentation Files

### 📖 `README.md` (Main Documentation)
- Overview and features
- Installation instructions
- Command reference
- Configuration guide
- Troubleshooting
- Future features

### 🚀 `QUICK_START.md` (Quick Setup)
- 5-minute setup guide
- Prerequisites checklist
- Minimal configuration
- Testing instructions
- Common first commands

### 📚 `INSTALLATION.md` (Detailed Setup)
- System requirements
- Step-by-step installation
- Docker setup
- Configuration details
- Testing procedures
- Troubleshooting guide

### 📋 `COMMANDS.md` (Command Reference)
- All commands documented
- Usage examples
- Permission levels
- Return values
- Tips and tricks

### ⚖️ `LICENSE`
- MIT License text
- Additional terms
- Copyright notice
- Disclaimer of warranties

---

## Utility Files

### 🔨 `Makefile`
Convenient commands for common tasks:
```bash
make help          # Show all commands
make install       # Install dependencies
make setup         # Setup environment
make test          # Test configuration
make run           # Run bot locally
make run-docker    # Run with Docker
make logs          # View logs
make clean         # Clean cache
make lint          # Code linting
make format        # Format code
```

### 📁 `.gitignore`
Excludes from git:
- `.env` file (sensitive data)
- `__pycache__` (Python cache)
- `downloads/` (cached music)
- `logs/` (log files)
- `venv/` (virtual environment)
- IDE files (.vscode, .idea)

---

## Directories

### 📥 `downloads/`
- **Purpose:** Cache directory for downloaded music
- **Auto-created:** Yes
- **Cleanup:** Manual (songs cached for reuse)
- **Size:** Grows with usage

### 📋 `logs/`
- **Purpose:** Bot log files
- **Format:** Rolling logs (10MB each, 10 backups)
- **Location:** `logs/bot.log`
- **Auto-created:** Yes

### `.git/`
- **Purpose:** Git repository tracking
- **Auto-created:** On `git clone`
- **Contains:** Version history and branches

---

## Code Flow

```
1. Start: python bot.py
   ↓
2. Load config.py
   ├─ Load .env variables
   ├─ Initialize API credentials
   └─ Setup directories
   ↓
3. Initialize bot.py
   ├─ Create Pyrogram Client
   ├─ Register command handlers
   └─ Setup callback handlers
   ↓
4. Connect to services
   ├─ Connect MongoDB
   ├─ Connect to Telegram
   └─ Start listening for messages
   ↓
5. User sends command
   ├─ Command handler triggered
   ├─ Database operations
   ├─ Music operations
   └─ Response sent to user
```

---

## File Dependencies

```
bot.py
├── imports config.py
├── imports database.py
├── imports music_handler.py
├── imports helpers.py
└── uses advanced_commands.py

config.py
├── reads .env file
└── creates directories

database.py
├── uses MONGO_DB_URI from config.py
└── imports pymongo

music_handler.py
├── uses CACHE_DIR from config.py
└── uses logger_config.py

helpers.py
├── uses OWNER_ID, ADMIN_IDS from config.py
└── uses database.py for admin checks

test_config.py
├── tests all dependencies
└── validates .env file

Dockerfile
└── builds from requirements.txt

docker-compose.yml
├── references Dockerfile
├── references .env
└── creates mongodb service
```

---

## Adding New Features

### To add a new command:
1. Add handler in `bot.py` using `@app.on_message()`
2. Check permissions using `Filters` from `helpers.py`
3. Use `Database` methods for data operations
4. Format response using `MessageBuilder`
5. Document in `COMMANDS.md`

### To add database operations:
1. Add method in `Database` class in `database.py`
2. Use appropriate collection
3. Return formatted data
4. Add error handling

### To add advanced features:
1. Add method in `AdvancedMusicCommands` class
2. Implement feature logic
3. Handle errors with try/except
4. Return formatted messages

---

**Last Updated:** June 1, 2026  
**Bot Version:** 1.0.0
