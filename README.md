# 🎵 JunoXmusic - Telegram Advanced Music Bot

An advanced Telegram music bot (JunoXmusic - @Junomusic_bot) with voice chat support, queue management, comprehensive admin controls, and channel logging.

## ✨ Features

### 🎵 Music Playback
- Search and play music from YouTube
- Queue management (add, remove, clear)
- Current song information display
- Skip, pause, resume, stop controls
- Volume control
- Autoplay functionality
- Like/Dislike reactions

### 👮 Admin Controls
- Make/remove admins per chat
- Skip songs (admins only)
- Clear queue (admins only)
- Control playback (pause/resume/stop)
- Volume management
- Autoplay toggle

### 👑 Owner Commands
- Broadcast messages
- View all bot statistics
- Shutdown and restart bot
- User management

### 📊 Statistics & Tracking
- User statistics (commands used, last seen)
- Queue tracking
- User database
- Channel logging of important events

## 📋 Requirements

- Python 3.8+
- FFmpeg (for audio processing)
- MongoDB (for data storage)
- Telegram Bot Token
- Telegram API Credentials

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/musicc.git
cd musicc
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Install system dependencies:
```bash
# For Ubuntu/Debian
sudo apt-get install ffmpeg

# For macOS
brew install ffmpeg
```

### 3. Setup Telegram Credentials
1. Go to https://my.telegram.org/apps
2. Create a new application
3. Copy `API_ID` and `API_HASH`
4. Create a bot with @BotFather on Telegram
5. Copy the `BOT_TOKEN`

### 4. Setup Environment Variables
```bash
cp .env.example .env
# Edit .env with your credentials
nano .env
```

Example .env file:
```
API_ID=123456
API_HASH=abcdef1234567890abcdef1234567890
BOT_TOKEN=1234567890:ABCdefGHIjklmNOpqrsTUVwxyzABCdef
ASSISTANT_ACCOUNT=@your_assistant_bot
MONGO_DB_URI=mongodb://localhost:27017
DB_NAME=music_bot
OWNER_ID=123456789
ADMIN_IDS=123456789 987654321
LOGGER_CHANNEL_ID=-1001234567890  # Optional: Channel ID for logging
```

### 5. Setup MongoDB
```bash
# Using Docker
docker run -d -p 27017:27017 --name mongodb mongo

# Or install MongoDB locally
sudo apt-get install mongodb
```

### 6. Run the Bot
```bash
python bot.py
```

## 📖 Commands

### 🎵 Basic Music Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/play <song_name>` | Search and play a song | `/play Never Gonna Give You Up` |
| `/search <query>` | Search for songs | `/search Bohemian Rhapsody` |
| `/queue` | Show current queue | `/queue` |
| `/current` | Show currently playing song | `/current` |
| `/skip` | Skip current song (admin) | `/skip` |
| `/pause` | Pause playback (admin) | `/pause` |
| `/resume` | Resume playback (admin) | `/resume` |
| `/stop` | Stop music and clear queue (admin) | `/stop` |

### 👮 Admin Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/clearqueue` | Clear entire queue | `/clearqueue` |
| `/volume <1-100>` | Set volume level | `/volume 80` |
| `/autoplay <on/off>` | Toggle autoplay | `/autoplay on` |
| `/makeadmin` | Make user admin (reply) | Reply to user + `/makeadmin` |
| `/removeadmin` | Remove admin privileges (reply) | Reply to admin + `/removeadmin` |
| `/admins` | List all chat admins | `/admins` |

### 📊 User Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/stats` | Show your statistics | `/stats` |
| `/ping` | Check bot status | `/ping` |
| `/help` | Show help message | `/help` |

### 👑 Owner Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/broadcast <msg>` | Broadcast message | `/broadcast Hello everyone!` |
| `/shutdown` | Shutdown the bot | `/shutdown` |

## 🏗️ Project Structure

```
musicc/
├── bot.py                 # Main bot file with command handlers
├── config.py             # Configuration settings
├── database.py           # MongoDB operations
├── music_handler.py      # Music download and search
├── helpers.py            # Helper functions and filters
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🔐 Security Features

- **Owner Authentication**: Critical commands require owner verification
- **Admin Controls**: Per-chat admin management
- **User Tracking**: Database logging of user interactions
- **Input Validation**: Command input validation and sanitization
- **Error Handling**: Comprehensive error handling throughout

## 🛠️ Configuration

Edit `config.py` to customize:
- Maximum queue size
- Cache directory for downloads
- Log directory
- Database settings
- Admin and owner IDs

### Logger Channel (Optional)

The bot supports logging important events to a private channel. To enable this:

1. **Create a private channel** on Telegram
2. **Get the Channel ID**: 
   - Add bot to the channel
   - Send any message
   - Forward to @JsonDumpBot
   - Look for `"chat"` field (negative number)
3. **Add to .env**:
   ```
   LOGGER_CHANNEL_ID=-1001234567890
   ```

**Events logged to channel:**
- 🎵 Songs added to queue (with user and group info)
- 👮 Admin promotions and removals
- ⏭️ Songs skipped
- ⏹️ Queue cleared
- 🔴 Bot shutdown events
- ❌ Error messages

## 📝 Database Schema

### Users Collection
```json
{
  "user_id": 123456789,
  "username": "username",
  "last_seen": "2024-06-01T10:30:00",
  "commands_used": 42
}
```

### Queue Collection
```json
{
  "chat_id": -1001234567890,
  "url": "https://youtube.com/watch?v=...",
  "title": "Song Title",
  "added_by": "username",
  "added_at": "2024-06-01T10:30:00"
}
```

### Admins Collection
```json
{
  "user_id": 123456789,
  "chat_id": -1001234567890,
  "added_at": "2024-06-01T10:30:00"
}
```

## 🐛 Troubleshooting

### FFmpeg not found
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### MongoDB Connection Error
Ensure MongoDB is running:
```bash
# If using Docker
docker start mongodb

# If using system MongoDB
sudo systemctl start mongodb
```

### Bot Not Responding
1. Check API credentials in `.env`
2. Verify bot token is correct
3. Check internet connection
4. View logs for error messages

## 📦 Dependencies

- **pyrogram**: Telegram Bot Framework
- **yt-dlp**: YouTube download library
- **python-dotenv**: Environment configuration
- **pymongo**: MongoDB driver
- **requests**: HTTP library
- **TgCrypto**: Telegram encryption

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This bot is for educational purposes. Make sure to:
- Follow Telegram's terms of service
- Respect copyright laws
- Use appropriate music sources
- Not spam or abuse the bot

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section
2. Review existing GitHub issues
3. Create a new issue with details

## 🚀 Future Features

- [ ] Lyrics display
- [ ] Music recommendations
- [ ] Playlist support
- [ ] Spotify integration
- [ ] SoundCloud support
- [ ] Audio effects/equalizer
- [ ] Multi-language support
- [ ] Web dashboard

## 👨‍💻 Author

Created with ❤️ for music lovers

---

**Last Updated**: June 1, 2026