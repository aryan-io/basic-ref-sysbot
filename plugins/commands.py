from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.buttons import *

# Function to register commands
def register_commands(app: Client, db):

    @app.on_message(filters.command("start"))
    async def start_command(client: Client, message: Message):
        user_id = message.from_user.id
        user_data = db.users.find_one({"_id": user_id})
        if not user_data:
            # New user registration
            db.users.insert_one({
                "_id": user_id,
                "username": message.from_user.username,
                "referrals": 0
            })

        await message.reply(
            "Welcome to the bot! Use the buttons below for more info.",
            reply_markup=start_buttons()
        )

    @app.on_message(filters.command("my_refs"))
    async def my_refs_command(client: Client, message: Message):
        user_id = message.from_user.id
        user_data = db.users.find_one({"_id": user_id})
        if user_data:
            referral_count = user_data.get("referrals", 0)
            await message.reply(f"You have referred {referral_count} users.")
        else:
            await message.reply("You are not registered in the system.")
