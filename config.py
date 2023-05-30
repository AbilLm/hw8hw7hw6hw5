from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler()

storage = MemoryStorage()
load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

