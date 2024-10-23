from pyrogram import Client
from plugins.commands import register_commands
from plugins.callback import register_callbacks
import os
import asyncio
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["telegram_bot"]  # Database name

# API and bot token from Telegram
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Create the bot client
app = Client("referral_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register commands and callbacks
register_commands(app, db)
register_callbacks(app, db)

# Main function to run the bot and the background task
async def main():
    await app.start()

    # Keep the bot running
    await app.idle()

    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
