from aiogram import executor
from config import dp
from handlers.picture import pic
from handlers.start import start
from handlers import fsm_anketa
from db import bot_db
from config import scheduler
from handlers.notific import handle_scheduler

scheduler.start()



bot_db.register_handlers_db(dp)

if __name__ == "__main__":
    dp.register_message_handler(pic, commands=['picture'])
    dp.register_message_handler(handle_scheduler, commands=['sche'])
    dp.register_message_handler(start, commands=['start'])
    fsm_anketa.register_fsm_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
