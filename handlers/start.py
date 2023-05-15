from aiogram import types



async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton('магазин', url= 'https://www.petshop.ru'),
        types.InlineKeyboardButton("о нас", url= 'https://www.petshop.ru/about/')
    )
    await message.answer("PETSHOP",
                         reply_markup=kb)