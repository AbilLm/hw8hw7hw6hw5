from aiogram import executor
from config import dp
from handlers.picture import pic
from handlers.start import start





if __name__ == "__main__":
    dp.register_message_handler(pic, commands=['picture'])
    dp.register_message_handler(start, commands=['start'])
    executor.start_polling(dp, skip_updates=True)
