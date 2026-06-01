#!/bin/bash

# Telegram Music Bot Startup Script

echo "🎵 Telegram Music Bot Starter"
echo "=============================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    exit 1
fi

# Check FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg is not installed!"
    echo "   Install with: sudo apt-get install ffmpeg"
fi

# Check .env file
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "   Please copy .env.example to .env and fill in your credentials"
    exit 1
fi

# Check requirements
echo "📦 Checking dependencies..."
pip install -r requirements.txt -q

# Create directories
mkdir -p downloads logs

# Start the bot
echo "✅ Starting Music Bot..."
python3 bot.py
