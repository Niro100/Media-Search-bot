import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ['AUTH_USERS'].split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi  {first_name}  {last_name}

 I'm NFLK Movie Search bot.

Hi 😉 ඔයාට ඕන Movie එක ලබා ගන්න මාව භාවිත කරන්න. **

Here you can search Movies in inline mode. Just press following buttons and start searching.

ඔයාලට අවශ්‍ය Movies ලබාගන්න පහත ඉන්ලයින් බටන් එක යුස් කරන්න 👇

ඒක ටච් කරාම මැසෙජ් ටයිප් කරන තැන එන සර්ච් ඔප්ශන් එක යුස් කරලා ඔයාට ඕන Movie එක හොයා ගන්න.
"""

SHARE_BUTTON_TEXT = """
Checkout {username} for searching files.

Hey 🙋‍♂ If you want get Inline Search Sinhala mod for your owne Bot 🤖

Plz contact me :- @Delta_theta

Project of SSB
"""
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
