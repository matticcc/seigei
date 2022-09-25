from pyrogram import Client, filters
from pyrogram.types import Message, User

api_id = 9244050
api_hash = "cb30d6a57834b81bf1bcd28843a81e02"
bot = "5733692416:AAG7xSZmCesQQ0GFFeYzS2Xoua-nJY6b72w" # Token

bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot)

@bot.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await message.reply("Sei Gay!")
