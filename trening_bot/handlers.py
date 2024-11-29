# handlers.py
from aiogram import types
from aiogram.dispatcher import Dispatcher
from subscription import check_subscription
from exercises import get_exercise_categories, get_exercise_video
from config import CHANNEL_ID

async def start_command(message: types.Message):
    await message.answer("Привет! Пожалуйста, подпишитесь на наш канал: " + CHANNEL_ID)
    # Проверка подписки
    if await check_subscription(message.from_user.id, message.bot):
        await show_main_menu(message)
    else:
        await message.answer("Вы не подписаны на канал. Пожалуйста, подпишитесь.")

async def show_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Выбор упражнения"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

async def choose_exercise(message: types.Message):
    categories = get_exercise_categories()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        keyboard.add(types.KeyboardButton(category))
    keyboard.add(types.KeyboardButton("Назад"))
    await message.answer("Выберите категорию упражнений:", reply_markup=keyboard)

async def show_exercises(message: types.Message):
    category = message.text
    exercises = video_manager.get_exercises(category)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for exercise in exercises:
        keyboard.add(types.KeyboardButton(exercise))
    keyboard.add(types.KeyboardButton("Назад"))
    await message.answer(f"Выберите упражнение из категории {category}:", reply_markup=keyboard)

async def show_video(message: types.Message):
    exercise = message.text
    category = ...  # Получите категорию из контекста
    video_url = get_exercise_video(category, exercise)
    await message.answer(f"Вот видео с упражнением {exercise}: {video_url}")
