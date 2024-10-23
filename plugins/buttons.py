from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_buttons():
    buttons = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [
            InlineKeyboardButton("Developer", url="https://t.me/your_username"),
            InlineKeyboardButton("Updates", url="https://t.me/your_channel")
        ]
    ]
    return InlineKeyboardMarkup(buttons)

def referral_buttons(referral_link):
    buttons = [
        [
            InlineKeyboardButton("Share Referral Link", url=referral_link)
        ]
    ]
    return InlineKeyboardMarkup(buttons)
