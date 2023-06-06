from aiogram import types
from config import bot, scheduler
from aiogram.types import Message

async def handle_scheduler(message:Message):
    scheduler.add_job(
        send_notiflication,
        'cron',
        day_of_week='last mon',
        hour='22',
        args=(message.from_user.id, message.text)
    )
    await message.answer('хорошо напомню')

async def send_notiflication(chat_id:int, text:str):
    await bot.send_message(chat_id=chat_id, text=text)

async def cancle_notif(message: types.Message):
    scheduler.remove_job(job_id=message.from_user.id)
    await message.answer('не буду напоминать')
