# Main configuration file

# Mandatory Variables
API_ID = "27064328" # Replace with your actual Telegram API ID
API_HASH = "7be1392c2fe5ebf4fc3228706fbfb504"  # Replace with your actual Telegram API Hash
BOT_TOKEN = "your_bot_token_here"  # Replace with your actual Bot Token
OWNER_ID = "5019668523"  # Replace with your actual Owner ID
# Database
DATABASE_URL = "mongodb+srv://tabolo8539:0evqZDV4fC5fD17c@cluster0.cw8zxus.mongodb.net/?retryWrites=true&w=majority"  # Replace with your actual database URL

AUTH_CHAT = "-1002757806665" # Replace with your actual auth chat ID. You can use multiple IDs separated by ( space ).
LOGS_CHAT = "-1002495255166" # Replace with your actual logs chat ID
POST_CHAT = "-1002458070966" # Replace with your actual post chat ID

ADMIN_USERNAME = "TonyStark75" # Replace with your admin username
ADMIN_PASSWORD = "Tony2006" # Replace with your admin password


SITE_SECRET = "your_secret_key" # Replace with your site secret key
TMDB_API_KEY = "bf388abad0e6e262e3fdd564f4a91c82" # Replace with your TMDB API key

# Optional Variables

# If you want to use multiple bot tokens, uncomment the MULTI_TOKENS dictionary and add your tokens. this aditional bots will speed up the process of downloading and streaming files.
MULTI_TOKENS = {
    # 1: "BOT_TOKEN_1_HERE",
    # 2: "BOT_TOKEN_2_HERE",
    # Add more tokens as needed
}
DELETE_AFTER_MINUTES = 10 # Set the number of minutes after which files will be deleted from user message
POST_UPDATES = True # Set to True if you want to post updates in the post chat
USE_CAPTION = False # Set to True if you want to use captions for posts instead of file names.

# Port configuration
import os
PORT = int(os.environ.get("PORT", 6519))
















# (Don't touch this unless you know what you're doing)
SUDO_USERS = [int(x) for x in (OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in (AUTH_CHAT).split()]
