import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("MANAGER_CHAT_ID")

CHAT_ID = int(CHAT_ID)

bot = Bot(token=TOKEN)
dp = Dispatcher()


keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Оставить заявку")]], 
    resize_keyboard=True
)

@dp.message(lambda message: message.text == "/start")
async def start(message: types.Message):
    await message.answer("Привет! Оставьте заявку, и мы с вами свяжемся.", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Оставить заявку")
async def request_info(message: types.Message):
    await message.answer("Напишите вашу заявку в одном сообщении.")

@dp.message()
async def receive_request(message: types.Message):
    text = f"📩 Новая заявка от @{message.from_user.username} ({message.from_user.id}):\n\n{message.text}"
    
    print(f"Отправка сообщения в чат: {CHAT_ID}")
    
    await bot.send_message(CHAT_ID, text)
    await message.answer("Спасибо за информацию о вашем проекте! Мы приняли вашу заявку и скоро с вами свяжемся!", reply_markup=keyboard)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
