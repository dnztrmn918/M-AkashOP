import lyricsgenius
from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app

# Genius API token - apna khud ka token yahan daalo
GENIUS = lyricsgenius.Genius("DRiDUF93wpO-UOz-3JBy8Tj510sOW0Exj6cXmBhUqQxaGlFb1qnHt3rWPsfHffRL", skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])

@app.on_message(filters.command(["lyrics", "lyric"]) & filters.private)
async def get_lyrics(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("🎵 Please provide a song name!\nUsage: `/lyrics song name`")

    song_name = " ".join(message.command[1:])
    await message.reply("🔍 Searching lyrics...")

    try:
        song = GENIUS.search_song(song_name)
        if song:
            lyrics = song.lyrics
            if len(lyrics) > 4096:
                for i in range(0, len(lyrics), 4096):
                    await message.reply(lyrics[i:i+4096])
            else:
                await message.reply(lyrics)
        else:
            await message.reply("❌ Lyrics not found.")
    except Exception as e:
        await message.reply(f"🚫 Error: {str(e)}")
