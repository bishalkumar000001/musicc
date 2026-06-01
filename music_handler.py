# Music utility functions
import os
import subprocess
from yt_dlp import YoutubeDL
from config import CACHE_DIR
import logging

logger = logging.getLogger(__name__)

class MusicHandler:
    @staticmethod
    def download_audio(url):
        """Download audio from YouTube or other sources"""
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(CACHE_DIR, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                logger.info(f"Downloading audio from: {url}")
                info = ydl.extract_info(url, download=True)
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown'),
                    'thumbnail': info.get('thumbnail', None),
                    'url': url
                }
        except Exception as e:
            logger.error(f"Error downloading audio: {str(e)}")
            return None
    
    @staticmethod
    def search_song(query):
        """Search for songs"""
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'no_warnings': True,
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                logger.info(f"Searching for: {query}")
                results = ydl.extract_info(f"ytsearch:{query}", download=False)
                if results and 'entries' in results:
                    return results['entries'][0]
        except Exception as e:
            logger.error(f"Error searching song: {str(e)}")
            return None
    
    @staticmethod
    def get_file_path(title):
        """Get the file path for a downloaded song"""
        file_path = os.path.join(CACHE_DIR, f"{title}.mp3")
        if os.path.exists(file_path):
            return file_path
        return None
    
    @staticmethod
    def delete_audio(file_path):
        """Delete audio file"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Deleted: {file_path}")
                return True
        except Exception as e:
            logger.error(f"Error deleting file: {str(e)}")
        return False
    
    @staticmethod
    def get_duration(file_path):
        """Get duration of audio file"""
        try:
            result = subprocess.run(
                ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                 '-of', 'default=noprint_wrappers=1:nokey=1:noprint_wrappers=1', file_path],
                capture_output=True, text=True
            )
            return float(result.stdout.strip())
        except Exception as e:
            logger.error(f"Error getting duration: {str(e)}")
            return 0
