import asyncio
import aiogram
from aiogram import types
from aiogram.filters import command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
import config
from config import token
import IDK
bot = Bot(token=config.token)

dp = Dispatcher()

@dp.message(command.CommandStart())
async def get_start(message: types.Message):

    await message.reply("""
Привет, пользователь!
Этот телеграмм бот поможет тебе выбрать фильм.
просто введи:
/recommend <жанр> <год>
P.S если нужна информация по жанрам и годам введи команду /Info
    """)



