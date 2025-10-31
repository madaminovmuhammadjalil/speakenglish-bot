import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from getdif import getdifinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = "8351307663:AAE6GivAO5d8Dzx1pU_tzTzOWk8TxwJXwtE"

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start va /help komandasi uchun handler
@dp.message(Command("start", "help"))
async def send_welcome(message: Message):
    await message.answer("english bot")

# Oddiy echo handler
@dp.message()
async def echo_message(message: Message):
    response = len(message.text.split())
    lang = await translator.detect(message.text)
    if response>1:
        if lang=="en":
            response = await translator.translate(message.text,dest="uz",src="en")
            await message.reply(response.text)
        else:
            response = await translator.translate(message.text, dest="en", src="uz")
            await message.reply(response.text)
    else:
        response = getdifinitions(message.text)
        if "audioFile" in response:
            await message.answer(response["definitions"])
            await message.reply_voice(response["audioFile"])
        else:
            await message.answer(response["definitions"])

# Asosiy ishga tushirish funksiyasi
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
