from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

def register_callbacks(app: Client, db):
    
    @app.on_callback_query(filters.regex("help"))
    async def help_callback(client: Client, callback_query: CallbackQuery):
        await callback_query.answer()
        await callback_query.message.edit_text(
            "This is the help section. Here's how to use the bot..."
        )

    @app.on_callback_query(filters.regex("about"))
    async def about_callback(client: Client, callback_query: CallbackQuery):
        await callback_query.answer()
        await callback_query.message.edit_text(
            "This bot was created to demonstrate a referral system."
        )
