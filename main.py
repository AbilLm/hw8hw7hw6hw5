from aiogram import executor, types
from config import dp
from handlers.picture import pic
from handlers.start import start
from handlers import fsm_anketa
from db import bot_db
from config import scheduler
from ban_bot import handle_message

scheduler.start()



bot_db.register_handlers_db(dp)

if __name__ == "__main__":
    dp.register_message_handler(handle_message, content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(pic, commands=['picture'])
    dp.register_message_handler(handle_scheduler, commands=['sche'])
    dp.register_message_handler(start, commands=['start'])
    fsm_anketa.register_fsm_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
