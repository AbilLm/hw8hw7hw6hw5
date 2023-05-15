from aiogram import types


async def pic(message: types.Message):
    with open('media/img.png', 'rb') as photo:
        await message.answer_photo(photo)