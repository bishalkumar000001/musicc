# Helper filters and utilities
from config import ADMIN_IDS, OWNER_ID, BOT_NAME, BOT_USERNAME
from database import Database
import logging

logger = logging.getLogger(__name__)

class Filters:
    @staticmethod
    def is_admin(client, message):
        """Check if user is admin"""
        user_id = message.from_user.id
        chat_id = message.chat.id
        return (user_id == OWNER_ID or 
                user_id in ADMIN_IDS or 
                Database.is_admin(user_id, chat_id))
    
    @staticmethod
    def is_owner(client, message):
        """Check if user is owner"""
        return message.from_user.id == OWNER_ID
    
    @staticmethod
    def is_group(client, message):
        """Check if message is from group"""
        return message.chat.type in ['group', 'supergroup']

class Utils:
    @staticmethod
    def format_duration(seconds):
        """Format seconds to MM:SS or HH:MM:SS"""
        if seconds is None:
            return "Unknown"
        seconds = int(seconds)
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        if hours > 0:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"
    
    @staticmethod
    def truncate_text(text, length=100):
        """Truncate text to specific length"""
        if len(text) > length:
            return text[:length-3] + "..."
        return text

class MessageBuilder:
    @staticmethod
    def build_help_message():
        """Build help message with all commands"""
        help_text = f"""
🎵 **{BOT_NAME} - HELP**
@{BOT_USERNAME}

**📍 Basic Commands:**
/play <song_name> - Play a song
/pause - Pause current song
/resume - Resume playing
/stop - Stop and clear queue
/skip - Skip current song
/current - Show current song info
/queue - Show music queue
/search <song_name> - Search for songs

**📊 User Commands:**
/stats - Show your stats
/ping - Check bot status
/help - Show this help message

**👮 Admin Commands:**
/makeadmin @user - Make someone admin
/removeadmin @user - Remove admin privileges
/admins - List all admins
/clearqueue - Clear entire queue
/volume <1-100> - Set volume (admins only)
/autoplay <on/off> - Toggle autoplay (admins only)

**👑 Owner Commands:**
/broadcast <message> - Broadcast message
/stats_all - Get all bot stats
/shutdown - Stop the bot
/restart - Restart the bot

**💡 Tips:**
- Use /play to search and play songs from YouTube
- Add multiple songs to queue with /play
- Admins can control playback in their chat
- React with 👍 to songs you like
        """
        return help_text

    @staticmethod
    def build_queue_message(queue_items):
        """Build queue display message"""
        if not queue_items:
            return "❌ Queue is empty"
        
        text = "🎵 **QUEUE**\n\n"
        for i, item in enumerate(queue_items[:10], 1):
            title = Utils.truncate_text(item.get('title', 'Unknown'), 50)
            added_by = item.get('added_by', 'Unknown')
            text += f"{i}. {title}\n   └ By: {added_by}\n"
        
        if len(queue_items) > 10:
            text += f"\n... and {len(queue_items) - 10} more songs"
        
        return text
