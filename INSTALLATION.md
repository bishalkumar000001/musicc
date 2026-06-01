# 🚀 Installation Guide

Complete step-by-step guide to install and run the Telegram Music Bot.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Installation](#local-installation)
3. [Docker Installation](#docker-installation)
4. [Configuration](#configuration)
5. [Testing](#testing)
6. [Running the Bot](#running-the-bot)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements
- **OS:** Linux, macOS, or Windows (with WSL2)
- **Python:** 3.8 or higher
- **Disk Space:** 500MB minimum
- **RAM:** 512MB minimum
- **Internet:** Required for Telegram and YouTube APIs

### Required Accounts
1. **Telegram Account** (personal)
2. **Telegram Bot Token** (from @BotFather)

### Tools to Install

#### Option 1: Traditional Installation

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
sudo apt-get install ffmpeg
sudo apt-get install mongodb
```

**macOS:**
```bash
brew install python3
brew install ffmpeg
brew install mongodb-community
```

**Windows (PowerShell as Admin):**
```powershell
# Install Chocolatey first if not installed
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install tools
choco install python ffmpeg mongodb
```

#### Option 2: Docker Installation (Recommended)
```bash
# Install Docker
# Ubuntu/Debian
sudo apt-get install docker.io docker-compose

# macOS
brew install docker docker-compose

# Windows: Download Docker Desktop from https://www.docker.com/products/docker-desktop
```

---

## Local Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/musicc.git
cd musicc
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Get Telegram Credentials

**Get API ID and API Hash:**
1. Go to https://my.telegram.org/apps
2. Login with your Telegram account
3. Click "Create Application"
4. Fill in the required fields
5. Copy your `API_ID` and `API_HASH`

**Get Bot Token:**
1. Open Telegram and search for `@BotFather`
2. Send `/start` command
3. Send `/newbot` command
4. Follow the prompts to create a bot
5. Copy the bot token

### Step 5: Create Environment File
```bash
# Copy example file
cp .env.example .env

# Edit with your credentials
nano .env
# or use any text editor
```

**Fill in .env file:**
```bash
API_ID=123456
API_HASH=abcdef1234567890abcdef1234567890
BOT_TOKEN=1234567890:ABCdefGHIjklmNOpqrsTUVwxyzABCdef
ASSISTANT_ACCOUNT=@your_assistant_bot
MONGO_DB_URI=mongodb://localhost:27017
DB_NAME=music_bot
OWNER_ID=123456789
ADMIN_IDS=123456789 987654321
```

### Step 6: Start MongoDB
```bash
# Check if MongoDB is running
mongosh

# If not running, start it:
# Ubuntu/Debian:
sudo systemctl start mongodb

# macOS:
brew services start mongodb-community

# Windows:
net start MongoDB
```

### Step 7: Test Configuration
```bash
python test_config.py
```

You should see all tests pass with ✅ marks.

### Step 8: Run the Bot
```bash
python bot.py
```

Look for message: `✅ Bot started successfully!`

---

## Docker Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/musicc.git
cd musicc
```

### Step 2: Setup Environment
```bash
cp .env.example .env
# Edit .env with your credentials
nano .env
```

### Step 3: Build and Run
```bash
# Build the Docker image
docker-compose build

# Run the bot with MongoDB
docker-compose up -d
```

### Step 4: Monitor Logs
```bash
# View bot logs
docker-compose logs -f music_bot

# View MongoDB logs
docker-compose logs -f mongodb
```

### Step 5: Stop the Bot
```bash
docker-compose down
```

---

## Configuration

### Basic Configuration
Edit `.env` file with your settings:

```bash
# Telegram
API_ID=your_api_id                    # From https://my.telegram.org/apps
API_HASH=your_api_hash                # From https://my.telegram.org/apps
BOT_TOKEN=your_bot_token              # From @BotFather

# Database
MONGO_DB_URI=mongodb://localhost:27017
DB_NAME=music_bot

# Admin Settings
OWNER_ID=your_user_id                 # Your Telegram user ID
ADMIN_IDS=admin1 admin2 admin3        # Space-separated admin IDs
```

### Advanced Configuration
Edit `config.py`:

```python
MAX_QUEUE_SIZE = 100           # Maximum songs in queue
CACHE_DIR = "downloads"        # Directory for downloaded files
LOG_DIR = "logs"              # Directory for log files
```

### Find Your Telegram User ID
1. Send `/start` to @userinfobot
2. Bot will display your User ID
3. Copy and add to OWNER_ID in .env

---

## Testing

### Run Configuration Test
```bash
python test_config.py
```

Expected output:
```
✅ Tests Passed: 9
❌ Tests Failed: 0
📈 Success Rate: 100.0%

✅ All tests passed! You're ready to run the bot.
```

### Manual Testing in Telegram

1. **Find your bot:** Search for bot username in Telegram
2. **Send commands:** Try these commands:
   - `/start` - Should show welcome message
   - `/help` - Should show all commands
   - `/ping` - Should respond with online status
   - `/stats` - Should show your stats

---

## Running the Bot

### Option 1: Direct Execution
```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Run the bot
python bot.py
```

### Option 2: Using Start Script
```bash
chmod +x start.sh
./start.sh
```

### Option 3: Running in Background (Linux/macOS)
```bash
# Using nohup
nohup python bot.py > logs/bot.log 2>&1 &

# Using screen
screen -S music_bot
python bot.py
# Press Ctrl+A then D to detach
```

### Option 4: Docker
```bash
docker-compose up -d
```

### Check if Bot is Running
```bash
# Direct execution
ps aux | grep bot.py

# Docker
docker ps | grep music_bot
```

---

## Troubleshooting

### Issue: "API credentials invalid"
**Solution:**
1. Double-check API_ID and API_HASH in .env
2. Make sure bot token is correct
3. Verify credentials at https://my.telegram.org/apps

### Issue: "MongoDB connection refused"
**Solution:**
```bash
# Start MongoDB
# Ubuntu/Debian
sudo systemctl start mongodb

# macOS
brew services start mongodb-community

# Or using Docker
docker run -d -p 27017:27017 --name mongodb mongo
```

### Issue: "FFmpeg not found"
**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

### Issue: "ModuleNotFoundError: No module named 'pyrogram'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Bot not responding in Telegram"
**Solutions:**
1. Check internet connection
2. Verify bot token is correct
3. Check if bot is still running: `ps aux | grep bot.py`
4. View logs: `tail -f logs/bot.log`
5. Restart the bot

### Issue: "Permission denied when running start.sh"
**Solution:**
```bash
chmod +x start.sh
./start.sh
```

### Issue: "Queue not saving to database"
**Solution:**
1. Verify MongoDB is running
2. Check MONGO_DB_URI in .env
3. Verify database connection: `mongosh`

### Issue: "Audio file not downloading"
**Solution:**
1. Check internet connection
2. Verify FFmpeg is installed: `ffmpeg -version`
3. Check disk space: `df -h`
4. Verify downloads directory exists: `mkdir -p downloads`

---

## Upgrading

### Update Bot Code
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

### Backup Database
```bash
# Before major updates
mongodump --out backup_dir

# Restore if needed
mongorestore backup_dir
```

---

## Uninstallation

### Remove Local Installation
```bash
# Deactivate virtual environment
deactivate

# Remove directory
rm -rf musicc
```

### Remove Docker Installation
```bash
# Stop and remove containers
docker-compose down

# Remove images
docker rmi musicc_music_bot

# Remove volumes (careful - deletes database!)
docker volume rm musicc_mongodb_data
```

---

## Next Steps

1. ✅ Installation complete!
2. 📚 Read [COMMANDS.md](COMMANDS.md) to learn all commands
3. 🚀 Start the bot: `python bot.py`
4. 💬 Test the bot in Telegram
5. ⚙️ Customize configuration as needed

---

## Support

For issues:
1. Check [Troubleshooting](#troubleshooting) section
2. Review logs: `tail -f logs/bot.log`
3. Test configuration: `python test_config.py`
4. Create GitHub issue with detailed information

---

**Last Updated:** June 1, 2026  
**Bot Version:** 1.0.0
