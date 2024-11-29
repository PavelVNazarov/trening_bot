# bot.py
import logging
from config import API_TOKEN
from handlers import start_command, choose_exercise, show_exercises, show_video
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await start_command(message)

@dp.message_handler(lambda message: message.text == "Выбор упражнения")
async def choose_exercise_handler(message: types.Message):
    await choose_exercise(message)

@dp.message_handler(lambda message: message.text in get_exercise_categories())
async def show_exercises_handler(message: types.Message):
    await show_exercises(message)

@dp.message_handler(lambda message: message.text in video_manager.get_exercises(message.text))
async def show_video_handler(message: types.Message):
    await show_video(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)