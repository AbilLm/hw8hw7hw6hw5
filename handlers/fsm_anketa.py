from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext



class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    thank_you = State()


async def start_survey(message: Message):
    await Survey.name.set()
    await message.answer("Ваше имя:")


async def process_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Survey.next()
    await message.answer("Введите ваш возраст:")


async def proccess_age(message: Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("ВВодите только цифры")
    elif int(age) > 100 or int(age) < 10:
        await message.answer("Только от 8 и до 100")
    else:
        async with state.proxy() as data:
            data['age'] = int(age)

        await Survey.next()
        await message.answer("Укажите ваш пол", reply_markup=ReplyKeyboardMarkup().add(KeyboardButton('male')).add(KeyboardButton('female')))


async def process_gender(message: Message, state: FSMContext):
    if message.text not in ['male', 'female']:
        message.answer('Выберите один из данных гендоров')
    else:
        async with state.proxy() as data:
            data['gender'] = message.text.strip()

            person = data.as_dict()
            await message.answer(
                f"Подтвердите ваши данные: Имя: {person['name']}\n"
                f"Возраст:{person['age']}\n"
                f"Пол:{person['gender']}"

            )
        Survey.next()


async def thank_you(message: Message, state: FSMContext):
    async with state.proxy() as data:
        print(f"Data после state.finish {data}")
    # для очистки памяти
    await state.finish()
    await message.answer("Спасибо за уделенное время!")


async def cancel_survey(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за уделенное время!")


def register_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(start_survey, commands=["surv"])
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(proccess_age, state=Survey.age)
    dp.register_message_handler(process_gender, state=Survey.gender)
    dp.register_message_handler(thank_you, state=Survey.thank_you)
    dp.register_message_handler(cancel_survey, commands=["stop"], state="*")