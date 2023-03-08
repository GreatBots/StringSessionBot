from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Updates Channel ✨", url="https://t.me/MyOwnBots/")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About 🤖", callback_data="about")
        ]
    ]

    START = """
**Hey {}! Welcome to {}**

You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !
    """

    HELP = """
**Available Commands:**

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process

Thanks For Using This Bot 🤗
"""

    ABOUT = """
**About Me:** 
Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

**- Name :** Session String Generator

**- Channel :** @MyOwnBots

**- Framework :** [Pyrogram](https://docs.pyrogram.org)

**- Language :** [Python](https://www.python.org)

**- Developer :** @vi2k6
    """
