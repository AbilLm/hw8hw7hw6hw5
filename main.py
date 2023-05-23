from aiogram import executor
from config import dp
from handlers.picture import pic
from handlers.start import start
from handlers import fsm_anketa





if __name__ == "__main__":
    dp.register_message_handler(pic, commands=['picture'])
    dp.register_message_handler(start, commands=['start'])
    fsm_anketa.register_fsm_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
