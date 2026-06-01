# 🎵 Complete Commands Reference

## Table of Contents
- [Basic Commands](#basic-commands)
- [Admin Commands](#admin-commands)
- [Owner Commands](#owner-commands)
- [Advanced Features](#advanced-features)
- [User Feedback](#user-feedback)

---

## Basic Commands

### `/start`
Start the bot and display welcome message with inline buttons.

**Usage:** `/start`  
**Permission:** Everyone  
**Example Output:** Welcome message with Quick Access buttons

---

### `/help`
Display comprehensive help message with all available commands.

**Usage:** `/help`  
**Permission:** Everyone  
**Shows:** All commands categorized by type

---

### `/play <song_name>`
Search for a song on YouTube and add it to the queue.

**Usage:** `/play Never Gonna Give You Up`  
**Permission:** Everyone (in group chats)  
**Returns:** Song info (title, duration, uploader)  
**Actions:** Automatically searches YouTube and adds to queue

**Features:**
- Fuzzy search matching
- Shows song duration and uploader
- Like/Dislike buttons for feedback
- Automatic queue management

---

### `/search <query>`
Search for songs without immediately adding them to queue.

**Usage:** `/search Bohemian Rhapsody`  
**Permission:** Everyone  
**Returns:** Top search result with options to:
- ▶️ Play immediately
- ➕ Add to queue

**Features:**
- Thumbnail preview (if available)
- Multiple sorting options
- Direct play or queue options

---

### `/queue`
Display current music queue.

**Usage:** `/queue`  
**Permission:** Everyone  
**Shows:**
- Up to 10 songs in current queue
- Song titles and who added them
- Total songs remaining count

---

### `/current`
Show currently playing song information.

**Usage:** `/current`  
**Permission:** Everyone  
**Displays:**
- Song title
- Added by (username)
- Duration and progress
- Album art (if available)

---

### `/skip`
Skip the current song and move to next in queue.

**Usage:** `/skip`  
**Permission:** Admins only  
**Effect:** Removes current song from queue and starts next

---

### `/pause`
Pause current music playback.

**Usage:** `/pause`  
**Permission:** Admins only  
**Effect:** Music pauses without clearing queue

---

### `/resume`
Resume paused music.

**Usage:** `/resume`  
**Permission:** Admins only  
**Effect:** Continues playing from where it paused

---

### `/stop`
Stop music and clear entire queue.

**Usage:** `/stop`  
**Permission:** Admins only  
**Effect:** 
- Stops all playback
- Clears entire queue
- Resets player state

---

### `/stats`
Show your personal statistics.

**Usage:** `/stats`  
**Permission:** Everyone  
**Shows:**
- Username
- Commands used
- Last seen timestamp
- Total songs requested

---

### `/ping`
Check if bot is online and responsive.

**Usage:** `/ping`  
**Permission:** Everyone  
**Response:** Bot status indicator

---

## Admin Commands

Admin commands require user to be:
- Chat owner
- Bot owner
- Designated admin in that specific chat

### `/makeadmin`
Promote a user to admin status in the current chat.

**Usage:** 
1. Reply to user's message
2. Send: `/makeadmin`

**Permission:** Bot owner only  
**Effect:** User gets admin privileges in current chat  
**Notification:** User is notified about promotion

---

### `/removeadmin`
Remove admin privileges from a user.

**Usage:**
1. Reply to admin's message
2. Send: `/removeadmin`

**Permission:** Bot owner only  
**Effect:** User loses admin privileges in current chat

---

### `/admins`
List all admins in current chat.

**Usage:** `/admins`  
**Permission:** Everyone (info only)  
**Shows:**
- List of admin user IDs
- Date when promoted

---

### `/clearqueue`
Clear entire song queue for current chat.

**Usage:** `/clearqueue`  
**Permission:** Admins only  
**Effect:** Removes all songs from queue  
**Warning:** Action is permanent and immediate

---

### `/volume <1-100>`
Set playback volume level.

**Usage:** `/volume 75`  
**Permission:** Admins only  
**Range:** 1 (min) to 100 (max)  
**Effect:** Changes playback volume for entire chat

**Examples:**
- `/volume 50` - Set to 50%
- `/volume 100` - Maximum volume
- `/volume 1` - Minimum volume

---

### `/autoplay <on/off>`
Enable or disable automatic playback queue.

**Usage:** 
- `/autoplay on` - Enable autoplay
- `/autoplay off` - Disable autoplay

**Permission:** Admins only  
**Effect:** When enabled, bot automatically plays similar songs when queue is empty

---

## Owner Commands

Owner commands require user to be the bot owner (set in OWNER_ID).

### `/broadcast <message>`
Send message to all bot users.

**Usage:** `/broadcast Check out the new features!`  
**Permission:** Bot owner only  
**Scope:** All users who have interacted with bot
**Limitations:** Use responsibly to avoid spam

---

### `/stats_all`
Get comprehensive statistics about entire bot.

**Usage:** `/stats_all`  
**Permission:** Bot owner only  
**Shows:**
- Total users
- Total admins
- Total songs played
- Active chats
- Database size

---

### `/shutdown`
Gracefully shutdown the bot.

**Usage:** `/shutdown`  
**Permission:** Bot owner only  
**Effect:**
- Stops all current playback
- Saves all data
- Closes database connections
- Exits cleanly

---

### `/restart`
Restart the bot process.

**Usage:** `/restart`  
**Permission:** Bot owner only  
**Effect:**
- Saves current state
- Restarts bot service
- Reconnects to Telegram

---

## Advanced Features

### Music Reactions
On every song added to queue, you can:
- 👍 **Like** - Mark song as liked (for recommendations)
- 👎 **Dislike** - Mark as disliked (skip recommendations)

### Queue Position Management
- View position in queue
- See who added each song
- Remove your own songs from queue (future feature)

### Playback Controls
- Play/Pause
- Skip to next
- Previous song (future feature)
- Jump to specific position in queue (future feature)

### Search Features
- Fuzzy matching for typos
- Recent searches cache
- Top results sorting
- Duration filtering (future feature)

---

## User Feedback

### Inline Buttons
Most responses include interactive buttons for quick actions:
- **▶️ Play** - Immediately play song
- **➕ Queue** - Add to queue
- **👍 Like** - Mark as favorite
- **❌ Remove** - Remove from queue

### Status Messages
- ✅ Success messages
- ❌ Error messages with explanations
- ⏳ Loading indicators
- ⚠️ Warning messages

### Command Validation
Bot validates all input:
- Checks permissions before executing
- Provides helpful error messages
- Suggests correct usage for invalid commands
- Prevents abuse and spam

---

## Quick Tips

1. **No Admin but want to skip?** Request an admin to skip or use `/search` then `/play` different song
2. **Lost in queue?** Use `/queue` to see what's coming up
3. **Want to add multiple songs?** Just use `/play` multiple times
4. **Check bot status?** Use `/ping` anytime
5. **Need help?** Use `/help` to see all commands

---

## Command Aliases (Future)

Currently implementing common aliases:
- `/p` → `/play`
- `/s` → `/search`
- `/q` → `/queue`
- `/np` → `/current` (now playing)

---

## Error Messages & Solutions

| Error | Solution |
|-------|----------|
| "❌ Usage: /play <song_name>" | Make sure to include song name |
| "❌ Song not found!" | Try different search terms |
| "❌ Only admins can skip!" | Ask admin to skip or play different song |
| "❌ Queue is empty!" | Add songs with `/play` first |
| "❌ Only in group chats" | This command only works in groups |

---

**Last Updated:** June 1, 2026  
**Bot Version:** 1.0.0
