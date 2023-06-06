from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dp = Dispatcher(Bot, storage=storage)

maty = ['gitler', 'negr', 'chornyi']

async def handle_message(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    # Проверка, является ли пользователь администратором группы
    admins = await Bot.get_chat_administrators(message.chat.id)
    admin_ids = [admin.user.id for admin in admins]
    if user_id in admin_ids:
        # Если пользователь админ, отправить замечание
        await message.reply(f"Администратор {user_name}, не выражайтесь, сегдня у меня др.")
    else:
        #
        await message.reply(f"Пользователь {user_name} забанен.")
        await Bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)
