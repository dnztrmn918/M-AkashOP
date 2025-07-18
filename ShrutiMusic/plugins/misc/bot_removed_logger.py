from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOGGER_ID  # <- LOGGER_ID must be defined in config.py

@app.on_message(filters.left_chat_member)
async def bot_removed_from_group(client: Client, message: Message):
    # Check if the bot itself was removed from the group
    bot_info = await client.get_me()
    if message.left_chat_member.id == bot_info.id:
        chat_title = message.chat.title or "Unnamed Group"
        chat_id = message.chat.id
        await client.send_message(
            LOGGER_ID,
            f"🚫 Bot has been **removed** from a group!\n\n"
            f"📛 Group Name: `{chat_title}`\n🆔 Group ID: `{chat_id}`"
        )
