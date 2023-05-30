
from config import bot, scheduler
from aiogram.types import Message



async def handle_scheduler(message:Message):
    scheduler.add_job(
        send_notiflication,
        'cron',
        day_of_week='tue',
        hour='17',
        args=(message.from_user.id, )
    )
    await message.answer('хорошо напомню')

async def send_notiflication(chat_id:int):
    await bot.send_message(chat_id=chat_id, text='напоминаюю')
