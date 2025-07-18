print("✅ Assistant welcome module loaded.")

from pyrogram import filters
from pyrogram.types import Message

from ShrutiMusic import app, userbot
from ShrutiMusic.core.userbot import assistants

WELCOME_TEXT = "👋 Welcome, {mention}!\n\nWelcome to {chat_title} 🎶\nUse /help to know my features!"

@app.on_message(filters.new_chat_members)
async def assistant_welcome(_, message: Message):
    for member in message.new_chat_members:
        if member.is_bot:
            continue  # skip bots

        if 1 not in assistants:
            return  # assistant not loaded

        ubot = userbot.one
        chat_id = message.chat.id
        chat_title = message.chat.title
        mention = member.mention(style="md")

        try:
            await ubot.send_message(
                chat_id,
                WELCOME_TEXT.format(mention=mention, chat_title=chat_title)
            )
        except Exception as e:
            print(f"[ASSISTANT ERROR] Failed to welcome: {e}")
