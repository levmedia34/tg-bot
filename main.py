import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("MANAGER_CHAT_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Клавиатура с кнопкой "Оставить заявку"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Оставить заявку"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Оставьте заявку, и мы с вами свяжемся.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Оставить заявку")
async def request_info(message: types.Message):
    await message.answer("Напишите вашу заявку в одном сообщении.")

@dp.message_handler()
async def receive_request(message: types.Message):
    text = f"📩 Новая заявка от @{message.from_user.username} ({message.from_user.id}):\n\n{message.text}"
    await bot.send_message(CHAT_ID, text)
    await message.answer("Спасибо за информацию о вашем проекте! Мы приняли вашу заявку и скоро с вами свяжемся!", reply_markup=keyboard)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()
