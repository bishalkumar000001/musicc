# Logging configuration
import logging
import logging.handlers
import os
from config import LOG_DIR

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name, level=logging.INFO):
    """Setup logger with file and console handlers"""
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(LOG_DIR, 'bot.log'),
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    file_handler.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Setup main logger
bot_logger = setup_logger('music_bot')
