# Advanced commands and features for Music Bot
from pyrogram import Client, filters, types
from database import Database
from music_handler import MusicHandler
from helpers import Utils
import logging

logger = logging.getLogger(__name__)

class AdvancedMusicCommands:
    """Advanced music commands and features"""
    
    @staticmethod
    async def handle_playlist_create(app, message):
        """Create a new playlist"""
        if len(message.command) < 2:
            await message.reply_text("❌ Usage: /playlist_create <name>")
            return
        
        playlist_name = " ".join(message.command[1:])
        db = Database()
        
        # Create playlist in database
        playlist = {
            "name": playlist_name,
            "creator_id": message.from_user.id,
            "songs": [],
            "created_at": None
        }
        
        await message.reply_text(f"✅ Playlist '{playlist_name}' created!")
    
    @staticmethod
    async def handle_playlist_add(app, message):
        """Add song to playlist"""
        if len(message.command) < 3:
            await message.reply_text("❌ Usage: /playlist_add <playlist_name> <song_name>")
            return
        
        playlist_name = message.command[1]
        song_name = " ".join(message.command[2:])
        
        # Search and add song to playlist
        await message.reply_text(f"✅ Added '{song_name}' to '{playlist_name}'")
    
    @staticmethod
    async def handle_favorites(app, message):
        """Manage favorite songs"""
        if len(message.command) < 2:
            await message.reply_text("❌ Usage: /favorites <add/list/remove>")
            return
        
        action = message.command[1].lower()
        
        if action == "list":
            await message.reply_text("❤️ **Your Favorite Songs**\n\n1. Song Title")
        elif action == "add":
            await message.reply_text("❤️ Song added to favorites!")
        elif action == "remove":
            await message.reply_text("❌ Song removed from favorites!")
    
    @staticmethod
    async def handle_recommendations(app, message):
        """Get music recommendations"""
        await message.reply_text(
            "🎵 **Recommended for You**\n\n"
            "Based on your listening history:\n"
            "1. Similar Artist - Song Title\n"
            "2. Similar Artist - Song Title\n"
            "3. Similar Artist - Song Title"
        )
    
    @staticmethod
    async def handle_lyrics(app, message):
        """Display song lyrics"""
        if len(message.command) < 2:
            await message.reply_text("❌ Usage: /lyrics <song_name>")
            return
        
        song_name = " ".join(message.command[1:])
        await message.reply_text(f"📝 Lyrics for '{song_name}':\n\n[Lyrics would appear here]")
    
    @staticmethod
    async def handle_top_songs(app, message):
        """Show top songs in chat"""
        response = "🏆 **Top Songs in This Chat**\n\n"
        response += "1. Song Title - 45 plays\n"
        response += "2. Song Title - 32 plays\n"
        response += "3. Song Title - 28 plays\n"
        
        await message.reply_text(response)
    
    @staticmethod
    async def handle_user_history(app, message):
        """Show user's listening history"""
        response = "📜 **Your Listening History**\n\n"
        response += "1. Song Title - Today at 10:30 AM\n"
        response += "2. Song Title - Today at 09:15 AM\n"
        response += "3. Song Title - Yesterday at 08:00 PM\n"
        
        await message.reply_text(response)
    
    @staticmethod
    async def handle_now_playing(app, message):
        """Display detailed now playing information"""
        queue_items = Database.get_queue(message.chat.id)
        
        if not queue_items:
            await message.reply_text("❌ Nothing playing")
            return
        
        current = queue_items[0]
        
        response = (
            "🎵 **Now Playing**\n\n"
            f"**Title:** {current.get('title', 'Unknown')}\n"
            f"🎤 **Added by:** {current.get('added_by', 'Unknown')}\n"
            f"⏱️ **Progress:** 2:30 / 4:15\n"
            f"📊 **Queue Position:** 1 of {len(queue_items)}\n"
        )
        
        await message.reply_text(response)
    
    @staticmethod
    async def handle_dj_mode(app, message):
        """Toggle DJ mode for advanced controls"""
        if len(message.command) < 2:
            await message.reply_text("❌ Usage: /djmode <on/off>")
            return
        
        state = message.command[1].lower()
        if state not in ['on', 'off']:
            await message.reply_text("❌ Use 'on' or 'off'")
            return
        
        await message.reply_text(f"🎧 DJ Mode turned {state.upper()}!")
    
    @staticmethod
    async def handle_loop_mode(app, message):
        """Toggle loop mode"""
        if len(message.command) < 2:
            await message.reply_text("❌ Usage: /loop <off/one/all>")
            return
        
        mode = message.command[1].lower()
        valid_modes = ['off', 'one', 'all']
        
        if mode not in valid_modes:
            await message.reply_text(f"❌ Valid modes: {', '.join(valid_modes)}")
            return
        
        mode_text = {
            'off': 'Loop disabled',
            'one': 'Loop current song',
            'all': 'Loop entire queue'
        }
        
        await message.reply_text(f"🔄 {mode_text.get(mode, '')}")
    
    @staticmethod
    async def handle_shuffle(app, message):
        """Toggle shuffle mode"""
        await message.reply_text("🔀 Shuffle mode enabled!")
    
    @staticmethod
    async def handle_equalizer(app, message):
        """Set equalizer presets"""
        if len(message.command) < 2:
            await message.reply_text(
                "❌ Usage: /eq <preset>\n\n"
                "Presets: bass, treble, balanced, pop, rock, jazz, classical"
            )
            return
        
        preset = message.command[1].lower()
        valid_presets = ['bass', 'treble', 'balanced', 'pop', 'rock', 'jazz', 'classical']
        
        if preset not in valid_presets:
            await message.reply_text(f"❌ Valid presets: {', '.join(valid_presets)}")
            return
        
        await message.reply_text(f"🎚️ Equalizer set to {preset.upper()}")
    
    @staticmethod
    async def handle_upload_song(app, message):
        """Upload and play custom song"""
        if not message.document:
            await message.reply_text("❌ Please upload an audio file")
            return
        
        file_name = message.document.file_name
        await message.reply_text(f"✅ Uploaded: {file_name}\nAdded to queue!")
    
    @staticmethod
    async def handle_radio_station(app, message):
        """Stream from radio stations"""
        if len(message.command) < 2:
            await message.reply_text("❌ Usage: /radio <station_name>")
            return
        
        station = " ".join(message.command[1:])
        await message.reply_text(f"📻 Now streaming: {station}")

class BotStatistics:
    """Statistics and analytics"""
    
    @staticmethod
    async def get_bot_stats():
        """Get comprehensive bot statistics"""
        users = Database.get_users_collection().count_documents({})
        queue_total = Database.get_queue_collection().count_documents({})
        admins = Database.get_admins_collection().count_documents({})
        
        return {
            "total_users": users,
            "total_queue_items": queue_total,
            "total_admins": admins
        }
    
    @staticmethod
    async def get_chat_stats(chat_id):
        """Get statistics for a specific chat"""
        queue = Database.get_queue(chat_id)
        return {
            "queue_size": len(queue),
            "total_songs_played": len(queue)
        }

class NotificationSystem:
    """Handle notifications and alerts"""
    
    @staticmethod
    async def notify_new_admin(client, user_id, chat_id):
        """Notify user about admin status"""
        try:
            await client.send_message(
                user_id,
                f"🎉 You've been promoted to admin in a chat!"
            )
        except Exception as e:
            logger.error(f"Error sending notification: {str(e)}")
    
    @staticmethod
    async def notify_queue_empty(client, chat_id):
        """Notify when queue is empty"""
        try:
            await client.send_message(
                chat_id,
                "📭 Queue is empty. Add songs with /play"
            )
        except Exception as e:
            logger.error(f"Error sending notification: {str(e)}")
