import sqlite3
from pathlib import Path
from aiogram import Dispatcher, types
from config import bot, dp

DB_PATH = Path(__file__).parent.parent
DB_NAME = 'db.sqlite'
db = sqlite3.connect(DB_PATH / DB_NAME)
cursor = db.cursor()


def init_db():
    global db, cursor

def create_tables():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Genres (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        image_url TEXT,
        genre_id INTEGER,
        FOREIGN KEY(genre_id) REFERENCES Genres(id)
    )""")
    db.commit()

def insert_data():

    cursor.execute("""INSERT INTO Genres (name) VALUES
        ('Фантастика'),
        ('Романы'),
        ('Детективы')""")


    cursor.execute("""INSERT INTO Books (name, price, image_url, genre_id) VALUES
        ('Война и мир', 1500.00, 'media/img.png', 2),
        ('Мастер и Маргарита', 1200.00, 'media/img.png', 4),
        ('Дозоры', 1700.00, 'media/img.png', 1),
        ('Братья Карамазовы', 1600.00, 'media/img.png', 2),
        ('Азазель', 1000.00, 'media/img.png', 3)
    """)
    db.commit()


def drop_tables():
    cursor.execute("""DROP TABLE IF EXISTS Books""")
    cursor.execute("""DROP TABLE IF EXISTS Genres""")
    db.commit()


def fetch_books():
    # -- Fetch all books
    cursor.execute("""SELECT * FROM Books""")
    books = cursor.fetchall()
    # for b in books:
    #     print(b[1])
    return books


def keyboard(pr_id:int):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('купить', callback_data=f'buy_{pr_id}'))
    return kb

products = cursor.execute('SELECT * FROM Books').fetchall()

async def show_mag(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('вот все книги:', reply_markup=kb)
    list1 = list(products)
    for j in list1:
        await message.answer(j[1], reply_markup=keyboard(j[0]))

async def buy_prouct(call: types.CallbackQuery):
    id = call.data[4:]
    await call.answer(f"Вы купили Book {id}")


if __name__ == "__main__":
    init_db()
    drop_tables()
    create_tables()
    insert_data()
    fetch_books()

