# Database helper functions
from pymongo import MongoClient
from config import MONGO_DB_URI, DB_NAME
from datetime import datetime

client = MongoClient(MONGO_DB_URI)
db = client[DB_NAME]

class Database:
    @staticmethod
    def get_users_collection():
        return db["users"]
    
    @staticmethod
    def get_queue_collection():
        return db["queue"]
    
    @staticmethod
    def get_admins_collection():
        return db["admins"]
    
    @staticmethod
    def add_user(user_id, username):
        """Add or update user in database"""
        users = Database.get_users_collection()
        users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "user_id": user_id,
                    "username": username,
                    "last_seen": datetime.now(),
                    "commands_used": 0
                }
            },
            upsert=True
        )
    
    @staticmethod
    def add_to_queue(chat_id, song_url, song_title, added_by):
        """Add song to queue"""
        queue = Database.get_queue_collection()
        queue.insert_one({
            "chat_id": chat_id,
            "url": song_url,
            "title": song_title,
            "added_by": added_by,
            "added_at": datetime.now()
        })
    
    @staticmethod
    def get_queue(chat_id):
        """Get all songs in queue for a chat"""
        queue = Database.get_queue_collection()
        return list(queue.find({"chat_id": chat_id}))
    
    @staticmethod
    def remove_from_queue(chat_id, song_id):
        """Remove song from queue"""
        queue = Database.get_queue_collection()
        queue.delete_one({"_id": song_id, "chat_id": chat_id})
    
    @staticmethod
    def clear_queue(chat_id):
        """Clear queue for a chat"""
        queue = Database.get_queue_collection()
        queue.delete_many({"chat_id": chat_id})
    
    @staticmethod
    def add_admin(user_id, chat_id):
        """Add user as admin for a chat"""
        admins = Database.get_admins_collection()
        admins.update_one(
            {"user_id": user_id, "chat_id": chat_id},
            {"$set": {"user_id": user_id, "chat_id": chat_id, "added_at": datetime.now()}},
            upsert=True
        )
    
    @staticmethod
    def remove_admin(user_id, chat_id):
        """Remove admin privileges"""
        admins = Database.get_admins_collection()
        admins.delete_one({"user_id": user_id, "chat_id": chat_id})
    
    @staticmethod
    def is_admin(user_id, chat_id):
        """Check if user is admin"""
        admins = Database.get_admins_collection()
        return admins.find_one({"user_id": user_id, "chat_id": chat_id}) is not None
    
    @staticmethod
    def get_chat_admins(chat_id):
        """Get all admins for a chat"""
        admins = Database.get_admins_collection()
        return list(admins.find({"chat_id": chat_id}))
