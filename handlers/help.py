from aiogram import types

async def help_handler(message: types.Message):
    await message.send_message(message.from_user.id, 'я имею 4 команды:\n'
                                                   '/start - команда start должна приветствовать по имени\n'
                                                   '/myinfo -команда myinfo должна отправлять пользователю его данные(id, first_name, username)\n'
                                                   '/help - поможет с командами\n'
                                                   '/picture -  скинет фото котика\n')