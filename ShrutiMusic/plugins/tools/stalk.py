print("✅ stalk.py loaded")

import asyncio
import random

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory

from ShrutiMusic import app, userbot
from ShrutiMusic.core.userbot import assistants

@app.on_message(filters.command("sg") & filters.private)
async def stalk_user_history(client, message: Message):
    if len(message.text.split()) < 2 and not message.reply_to_message:
        return await message.reply("❗ Please provide a username, ID, or reply to a user.")

    # Get user ID or argument
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1]

    loading = await message.reply("<code>Processing request...</code>")

    try:
        user = await client.get_users(args)
    except Exception:
        return await loading.edit("❌ <code>Invalid user specified!</code>")

    # Select random Sangmata bot
    sangmata_bots = ["sangmata_bot", "sangmata_beta_bot"]
    selected_bot = random.choice(sangmata_bots)

    if 1 in assistants:
        ubot = userbot.one
    else:
        return await loading.edit("❌ <code>Userbot not initialized.</code>")

    # Send user ID to Sangmata bot
    try:
        query = await ubot.send_message(selected_bot, str(user.id))
        await query.delete()
    except Exception as e:
        return await loading.edit(f"❌ <code>{e}</code>")

    await asyncio.sleep(1.5)

    # Read stalk result
    try:
        async for stalk in ubot.search_messages(selected_bot):
            if not stalk or not stalk.text:
                continue
            await message.reply(stalk.text)
            break
        else:
            await message.reply("⚠️ No data found or bot unresponsive.")
    except Exception:
        await message.reply("⚠️ Failed to retrieve history from Sangmata bot.")

    # Clear chat history
    try:
        user_info = await ubot.resolve_peer(selected_bot)
        await ubot.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await loading.delete()
