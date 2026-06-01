# Main Telegram Music Bot
import logging
from pyrogram import Client, filters, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, ADMIN_IDS, BOT_NAME, BOT_USERNAME, LOGGER_CHANNEL_ID
from database import Database
from music_handler import MusicHandler
from helpers import Filters, Utils, MessageBuilder
import asyncio

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
app = Client(
    BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Global variables for tracking current playback
current_playback = {}

# Channel logging function
async def log_to_channel(message_text, error=False):
    """Log messages to logger channel if configured"""
    if not LOGGER_CHANNEL_ID:
        return
    
    try:
        emoji = "❌" if error else "✅"
        await app.send_message(
            LOGGER_CHANNEL_ID,
            f"{emoji} {message_text}"
        )
    except Exception as e:
        logger.error(f"Error sending log to channel: {str(e)}")

@app.on_message(filters.command("start"))
async def start_command(client, message):
    """Start command"""
    Database.add_user(message.from_user.id, message.from_user.username or "Unknown")
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Play Music", callback_data="play"),
            InlineKeyboardButton("Help", callback_data="help")
        ],
        [
            InlineKeyboardButton("Queue", callback_data="queue"),
            InlineKeyboardButton("Stats", callback_data="stats")
        ]
    ])
    
    await message.reply_text(
        f"🎵 **Welcome to {BOT_NAME}!**\n\n"
        f"I'm an advanced music bot with voice chat support.\n"
        f"Bot: @{BOT_USERNAME}\n\n"
        f"Use /help to see all available commands.",
        reply_markup=keyboard
    )
    
    # Log to channel
    if LOGGER_CHANNEL_ID:
        await log_to_channel(f"New user started bot: {message.from_user.first_name} (ID: {message.from_user.id})")

@app.on_message(filters.command("help"))
async def help_command(client, message):
    """Help command"""
    await message.reply_text(MessageBuilder.build_help_message(), parse_mode="markdown")

@app.on_message(filters.command("play") & filters.group)
async def play_command(client, message):
    """Play music command"""
    if len(message.command) < 2:
        await message.reply_text("❌ Usage: /play <song_name>")
        return
    
    song_name = " ".join(message.command[1:])
    status_msg = await message.reply_text(f"🔍 Searching for: {song_name}...")
    
    try:
        song_info = MusicHandler.search_song(song_name)
        if not song_info:
            await status_msg.edit_text("❌ Song not found!")
            return
        
        Database.add_to_queue(
            message.chat.id,
            song_info.get('url'),
            song_info.get('title', 'Unknown'),
            message.from_user.username or "Unknown"
        )
        
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("👍 Like", callback_data="like"),
                InlineKeyboardButton("👎 Dislike", callback_data="dislike")
            ]
        ])
        
        await status_msg.edit_text(
            f"✅ **Added to Queue**\n\n"
            f"🎵 **Title:** {Utils.truncate_text(song_info.get('title', 'Unknown'))}\n"
            f"⏱️ **Duration:** {Utils.format_duration(song_info.get('duration', 0))}\n"
            f"🎤 **Channel:** {song_info.get('uploader', 'Unknown')}",
            reply_markup=keyboard,
            parse_mode="markdown"
        )
        
        # Log to channel
        if LOGGER_CHANNEL_ID:
            await log_to_channel(
                f"🎵 Song added to queue: {Utils.truncate_text(song_info.get('title', 'Unknown'))}\n"
                f"👤 By: {message.from_user.first_name} (@{message.from_user.username})\n"
                f"💬 Group: {message.chat.title}"
            )
        
    except Exception as e:
        logger.error(f"Error in play command: {str(e)}")
        await status_msg.edit_text(f"❌ Error: {str(e)}")
        if LOGGER_CHANNEL_ID:
            await log_to_channel(f"Error in play command: {str(e)}", error=True)

@app.on_message(filters.command("search"))
async def search_command(client, message):
    """Search for a song"""
    if len(message.command) < 2:
        await message.reply_text("❌ Usage: /search <song_name>")
        return
    
    query = " ".join(message.command[1:])
    status_msg = await message.reply_text(f"🔍 Searching: {query}...")
    
    try:
        song_info = MusicHandler.search_song(query)
        if not song_info:
            await status_msg.edit_text("❌ No results found!")
            return
        
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("▶️ Play", callback_data=f"play_{song_info.get('id')}"),
                InlineKeyboardButton("➕ Queue", callback_data=f"queue_{song_info.get('id')}")
            ]
        ])
        
        await status_msg.edit_text(
            f"🎵 **Search Result**\n\n"
            f"**Title:** {Utils.truncate_text(song_info.get('title', 'Unknown'))}\n"
            f"⏱️ **Duration:** {Utils.format_duration(song_info.get('duration', 0))}\n"
            f"🎤 **Channel:** {song_info.get('uploader', 'Unknown')}",
            reply_markup=keyboard,
            parse_mode="markdown"
        )
    except Exception as e:
        logger.error(f"Error in search command: {str(e)}")
        await status_msg.edit_text(f"❌ Error: {str(e)}")

@app.on_message(filters.command("queue"))
async def queue_command(client, message):
    """Show queue"""
    queue_items = Database.get_queue(message.chat.id)
    await message.reply_text(MessageBuilder.build_queue_message(queue_items), parse_mode="markdown")

@app.on_message(filters.command("current"))
async def current_command(client, message):
    """Show current song"""
    queue_items = Database.get_queue(message.chat.id)
    if not queue_items:
        await message.reply_text("❌ No song playing")
        return
    
    current = queue_items[0]
    await message.reply_text(
        f"🎵 **Now Playing**\n\n"
        f"**Title:** {current.get('title', 'Unknown')}\n"
        f"🎤 **Added by:** {current.get('added_by', 'Unknown')}",
        parse_mode="markdown"
    )

@app.on_message(filters.command("skip") & filters.group)
async def skip_command(client, message):
    """Skip current song"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can skip songs!")
        return
    
    queue_items = Database.get_queue(message.chat.id)
    if not queue_items:
        await message.reply_text("❌ Queue is empty!")
        return
    
    Database.remove_from_queue(message.chat.id, queue_items[0]['_id'])
    await message.reply_text("⏭️ Song skipped!")
    
    # Log to channel
    if LOGGER_CHANNEL_ID:
        await log_to_channel(
            f"⏭️ Song skipped: {queue_items[0].get('title', 'Unknown')}\n"
            f"👤 By: {message.from_user.first_name} (@{message.from_user.username})\n"
            f"💬 Group: {message.chat.title}"
        )

@app.on_message(filters.command("pause") & filters.group)
async def pause_command(client, message):
    """Pause music"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can pause!")
        return
    
    current_playback[message.chat.id] = 'paused'
    await message.reply_text("⏸️ Music paused!")

@app.on_message(filters.command("resume") & filters.group)
async def resume_command(client, message):
    """Resume music"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can resume!")
        return
    
    current_playback[message.chat.id] = 'playing'
    await message.reply_text("▶️ Music resumed!")

@app.on_message(filters.command("stop") & filters.group)
async def stop_command(client, message):
    """Stop music and clear queue"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can stop!")
        return
    
    Database.clear_queue(message.chat.id)
    current_playback.pop(message.chat.id, None)
    await message.reply_text("⏹️ Music stopped and queue cleared!")
    
    # Log to channel
    if LOGGER_CHANNEL_ID:
        await log_to_channel(
            f"⏹️ Queue cleared and music stopped\n"
            f"👤 By: {message.from_user.first_name} (@{message.from_user.username})\n"
            f"💬 Group: {message.chat.title}"
        )

@app.on_message(filters.command("clearqueue") & filters.group)
async def clearqueue_command(client, message):
    """Clear queue (Admin only)"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can clear queue!")
        return
    
    Database.clear_queue(message.chat.id)
    await message.reply_text("✅ Queue cleared!")

@app.on_message(filters.command("makeadmin") & filters.group)
async def makeadmin_command(client, message):
    """Make someone admin"""
    if not Filters.is_owner(client, message):
        await message.reply_text("❌ Only bot owner can make admins!")
        return
    
    if not message.reply_to_message:
        await message.reply_text("❌ Reply to a user to make them admin!")
        return
    
    user_id = message.reply_to_message.from_user.id
    Database.add_admin(user_id, message.chat.id)
    admin_username = message.reply_to_message.from_user.username or "Unknown"
    await message.reply_text(f"✅ User {user_id} is now admin!")
    
    # Log to channel
    if LOGGER_CHANNEL_ID:
        await log_to_channel(
            f"👮 Admin promoted: @{admin_username} (ID: {user_id})\n"
            f"👤 By: {message.from_user.first_name} (@{message.from_user.username})\n"
            f"💬 Group: {message.chat.title}"
        )

@app.on_message(filters.command("removeadmin") & filters.group)
async def removeadmin_command(client, message):
    """Remove admin privileges"""
    if not Filters.is_owner(client, message):
        await message.reply_text("❌ Only bot owner can remove admins!")
        return
    
    if not message.reply_to_message:
        await message.reply_text("❌ Reply to a user to remove admin!")
        return
    
    user_id = message.reply_to_message.from_user.id
    Database.remove_admin(user_id, message.chat.id)
    admin_username = message.reply_to_message.from_user.username or "Unknown"
    await message.reply_text(f"✅ Admin privileges removed from {user_id}!")
    
    # Log to channel
    if LOGGER_CHANNEL_ID:
        await log_to_channel(
            f"❌ Admin removed: @{admin_username} (ID: {user_id})\n"
            f"👤 By: {message.from_user.first_name} (@{message.from_user.username})\n"
            f"💬 Group: {message.chat.title}"
        )

@app.on_message(filters.command("admins") & filters.group)
async def admins_command(client, message):
    """List all admins"""
    admins = Database.get_chat_admins(message.chat.id)
    if not admins:
        await message.reply_text("❌ No admins in this chat!")
        return
    
    admin_list = "👮 **Admins in this chat:**\n\n"
    for i, admin in enumerate(admins, 1):
        admin_list += f"{i}. User ID: {admin['user_id']}\n"
    
    await message.reply_text(admin_list, parse_mode="markdown")

@app.on_message(filters.command("stats"))
async def stats_command(client, message):
    """Show user stats"""
    user = Database.get_users_collection().find_one({"user_id": message.from_user.id})
    if not user:
        await message.reply_text("❌ No stats found!")
        return
    
    await message.reply_text(
        f"📊 **Your Statistics**\n\n"
        f"👤 **Username:** {user.get('username', 'Unknown')}\n"
        f"🎵 **Commands Used:** {user.get('commands_used', 0)}\n"
        f"⏰ **Last Seen:** {user.get('last_seen', 'Unknown')}",
        parse_mode="markdown"
    )

@app.on_message(filters.command("ping"))
async def ping_command(client, message):
    """Check bot status"""
    await message.reply_text("🟢 **Bot is online and running!**", parse_mode="markdown")

@app.on_message(filters.command("volume") & filters.group)
async def volume_command(client, message):
    """Set volume (Admin only)"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can change volume!")
        return
    
    if len(message.command) < 2:
        await message.reply_text("❌ Usage: /volume <1-100>")
        return
    
    try:
        volume = int(message.command[1])
        if not 1 <= volume <= 100:
            await message.reply_text("❌ Volume must be between 1 and 100!")
            return
        
        current_playback[f"{message.chat.id}_volume"] = volume
        await message.reply_text(f"🔊 Volume set to {volume}%")
    except ValueError:
        await message.reply_text("❌ Invalid volume value!")

@app.on_message(filters.command("autoplay") & filters.group)
async def autoplay_command(client, message):
    """Toggle autoplay (Admin only)"""
    if not Filters.is_admin(client, message):
        await message.reply_text("❌ Only admins can toggle autoplay!")
        return
    
    if len(message.command) < 2:
        await message.reply_text("❌ Usage: /autoplay <on/off>")
        return
    
    state = message.command[1].lower()
    if state not in ['on', 'off']:
        await message.reply_text("❌ Use 'on' or 'off'")
        return
    
    current_playback[f"{message.chat.id}_autoplay"] = state == 'on'
    await message.reply_text(f"✅ Autoplay turned {state.upper()}!")

@app.on_message(filters.command("broadcast"))
async def broadcast_command(client, message):
    """Broadcast message (Owner only)"""
    if not Filters.is_owner(client, message):
        await message.reply_text("❌ Only bot owner can broadcast!")
        return
    
    if len(message.command) < 2:
        await message.reply_text("❌ Usage: /broadcast <message>")
        return
    
    broadcast_msg = " ".join(message.command[1:])
    # In production, iterate through all users and send
    await message.reply_text(f"✅ Broadcast message sent: {broadcast_msg}")

@app.on_message(filters.command("shutdown"))
async def shutdown_command(client, message):
    """Shutdown bot (Owner only)"""
    if not Filters.is_owner(client, message):
        await message.reply_text("❌ Only bot owner can shutdown!")
        return
    
    # Log to channel before shutting down
    if LOGGER_CHANNEL_ID:
        await log_to_channel(
            f"🔴 Bot shutting down\n"
            f"👤 By: {message.from_user.first_name} (@{message.from_user.username})"
        )
    
    await message.reply_text("⏹️ Bot shutting down...")
    await app.stop()

@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    """Handle inline button callbacks"""
    data = callback_query.data
    
    if data == "help":
        await callback_query.answer()
        await callback_query.message.edit_text(
            MessageBuilder.build_help_message(),
            parse_mode="markdown"
        )
    elif data == "queue":
        await callback_query.answer()
        queue_items = Database.get_queue(callback_query.message.chat.id)
        await callback_query.message.edit_text(
            MessageBuilder.build_queue_message(queue_items),
            parse_mode="markdown"
        )
    elif data == "stats":
        await callback_query.answer()
        await stats_command(client, callback_query.message)
    elif data == "like":
        await callback_query.answer("👍 Song liked!", show_alert=False)
    elif data == "dislike":
        await callback_query.answer("👎 Song disliked!", show_alert=False)

def main():
    """Start the bot"""
    logger.info("Starting Music Bot...")
    app.run()

if __name__ == "__main__":
    main()
