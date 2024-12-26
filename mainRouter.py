import os
import random

from aiogram import Router, types
from dotenv import load_dotenv
from pyrogram import Client
from aiogram.filters.command import Command

from emotions import emotions

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
api_name = os.getenv("API_NAME")

main_router = Router()
app = Client(api_name, api_id, api_hash)

@main_router.message(Command('all'))
async def all_bot_commands(message: types.Message):
    chat_id = message.chat.id
    await pass_errors(chat_id, message)

async def get_members(chat_id):
    members = []
    async with app:
        async for member in app.get_chat_members(chat_id):
            members.append(member.user.username)
    return members

async def pass_errors(chat_id, message):
    try:
        message_for_all = await representation(await get_members(chat_id))
        emotion_message = add_emotion(message_for_all)
        await message.answer(text=emotion_message)
    except Exception as e:
        message_for_all = await representation(await get_members(chat_id))
        await message.answer(text=message_for_all)
def add_emotion(message):
    try:
        emotion = random.choice(emotions)
        message = message + f"\n{emotion}"
    except:
        pass
    return f"{message}"

async def representation(members):
    str_members = "\n".join(list(map(add_dog, members)))
    return str_members[:len(str_members)]


def add_dog(username):
    return f"@{username}"