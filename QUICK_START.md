# 🚀 Quick Start Guide

Get your Telegram Music Bot running in 5 minutes!

## Prerequisites Checklist

- ✅ Python 3.8+ installed
- ✅ FFmpeg installed
- ✅ MongoDB installed (or Docker)
- ✅ Telegram account
- ✅ Bot token from @BotFather

## Step-by-Step Setup

### 1️⃣ Get Bot Token (2 min)

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow prompts and copy your bot token
4. Search for `@userinfobot` and note your User ID

### 2️⃣ Clone and Configure (2 min)

```bash
# Clone repo
git clone https://github.com/yourusername/musicc.git
cd musicc

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env
```

**Minimum .env content:**
```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=your_user_id
```

Get `API_ID` and `API_HASH` from: https://my.telegram.org/apps

### 3️⃣ Install Dependencies (1 min)

```bash
# Using Makefile (recommended)
make install

# OR manually
pip install -r requirements.txt
```

### 4️⃣ Test Setup (Less than 1 min)

```bash
make test
```

If all tests pass ✅, you're ready!

### 5️⃣ Start the Bot

```bash
# Using Makefile
make run

# OR directly
python bot.py
```

## 🎉 Done! Test Your Bot

1. Open Telegram
2. Search for your bot
3. Send `/start`
4. Try commands:
   - `/help` - Show all commands
   - `/play Any Song Name` - Play music
   - `/queue` - Show queue

## Common First Commands

```
/play Bohemian Rhapsody      # Add song to queue
/search Never Gonna Give You Up  # Search songs
/queue                       # See what's coming
/current                     # What's playing now
/skip                        # Skip (admin only)
/stats                       # Your statistics
```

## Next Steps

1. **Make Admin:** Reply `/makeadmin` to a user to give them admin powers
2. **Read Docs:** Check [COMMANDS.md](COMMANDS.md) for all commands
3. **Deploy:** Use `docker-compose up` to run permanently

## Using Docker (Alternative)

```bash
# Setup
cp .env.example .env
nano .env  # Add your credentials

# Run
docker-compose up -d

# View logs
docker-compose logs -f music_bot

# Stop
docker-compose down
```

## Useful Make Commands

```bash
make help          # Show all commands
make setup         # Setup fresh installation
make run           # Start bot
make run-docker    # Start with Docker
make logs          # View logs
make clean         # Clean cache
```

## Troubleshooting

### Bot not responding?
```bash
# Check if running
ps aux | grep bot.py

# View logs
tail -f logs/bot.log

# Restart
make stop && make run
```

### FFmpeg error?
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### MongoDB error?
```bash
# Start MongoDB
sudo systemctl start mongodb

# Or use Docker
docker run -d -p 27017:27017 --name mongodb mongo
```

## File Structure

```
musicc/
├── bot.py              # Main bot
├── config.py           # Settings
├── database.py         # Database operations
├── helpers.py          # Helper functions
├── music_handler.py    # Music operations
├── requirements.txt    # Dependencies
├── .env.example        # Config template
├── Makefile            # Convenient commands
└── README.md           # Full documentation
```

## Features You Have

✨ **Music Features:**
- Search and play YouTube music
- Queue management
- Pause/Resume/Skip
- Volume control
- Like/Dislike reactions

👮 **Admin Features:**
- Promote/demote admins
- Control playback
- Clear queue
- Auto-play toggle

📊 **User Features:**
- View statistics
- See queue
- Like/unlike songs

## Need Help?

1. **Full Docs:** Read [README.md](README.md)
2. **All Commands:** Check [COMMANDS.md](COMMANDS.md)
3. **Setup Issues:** See [INSTALLATION.md](INSTALLATION.md)
4. **Test Config:** Run `make test`

## Performance Tips

- Use Docker for 24/7 hosting
- Set OWNER_ID to your ID for all features
- Add trusted users as admins
- Monitor disk space for downloads
- Restart weekly for stability

---

**Questions?** Check the docs or create a GitHub issue!

**Enjoy your music bot! 🎵🤖**
