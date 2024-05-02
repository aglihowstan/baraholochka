import telebot
from telebot import types
from keys import BOT_API_KEY
import sqlite3

bot = telebot.TeleBot(BOT_API_KEY)

file_info = None
size = None
disc = None
limit1 = {}
limit2 = {}
limit3 = {}
limit4 = {}
limit5 = {}
limit6 = {}
limit7 = {}
limit8 = {}
limit9 = {}
limit10 = {}
limit11 = {}
limit12 = {}
limit13 = {}
limit14 = {}
limit15 = {}
limit16 = {}
limit17 = {}
vibor = {}
A = None

def Save(message):
    global file_info
    try:
        file_info = bot.get_file (message.photo[len(message.photo )- 1].file_id)
        # downloaded_file = bot.download_file(file_info.file_path)
        # src='./photos/' + file_info.file_path.replace('photos/','')
        # fileid = file_info.file_path.replace('photos/','')
        # with open(src, 'wb') as new_file:
        #     new_file.write(downloaded_file)
        #     new_file.close()
        bot.send_message(message.chat.id, 'Введите размер(20)')
        bot.register_next_step_handler(message, Size)
    except TypeError:
        bot.send_message(message.chat.id, text='Отправьте фотку')
        bot.register_next_step_handler(message, Save)

def Size(message):
    global size
    size = message.text
    bot.send_message(message.chat.id, 'Введите описание(70)')
    bot.register_next_step_handler(message, Disc)

def Disc(message):
    global disc
    disc = message.text
    bot.send_message(message.chat.id, 'Введите тип(70)')
    bot.register_next_step_handler(message, Type)

def Type(message):
    type = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Смотреть одежду')
    button2 = types.KeyboardButton('Добавить одежду')
    button3 = types.KeyboardButton('Моя одежда')
    button4 = types.KeyboardButton('Корзина')
    markup.row(button)
    markup.row(button2)
    markup.row(button3, button4)
    conn = sqlite3.connect('clouth.db')
    cur = conn.cursor()
    downloaded_file = bot.download_file(file_info.file_path)
    src='./photos/' + file_info.file_path.replace('photos/','')
    fileid = file_info.file_path.replace('photos/','')
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        new_file.close()
    data = (f'{fileid}', f'{size}', f'{disc}', f'{type}')
    cur.execute(f'INSERT INTO wother(Photo, Size, Discription, Type ) VALUES{data};')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Товар успешно добавлен', reply_markup= markup)
    
    
@bot.message_handler(commands = ['start'])
def start(message):
    global list
    global A
    sslka = message.chat.id
    n = 0
    limit1[sslka] = n
    limit2[sslka] = n
    limit3[sslka] = n
    limit4[sslka] = n
    limit5[sslka] = n
    limit6[sslka] = n
    limit7[sslka] = n
    limit8[sslka] = n
    limit9[sslka] = n
    limit10[sslka] = n
    limit11[sslka] = n
    limit12[sslka] = n
    limit13[sslka] = n
    limit14[sslka] = n
    limit15[sslka] = n
    limit16[sslka] = n
    limit17[sslka] = n
    vibor[sslka] = 'g' 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Смотреть одежду')
    button2 = types.KeyboardButton('Добавить одежду')
    button3 = types.KeyboardButton('Моя одежда')
    button4 = types.KeyboardButton('Корзина')
    markup.row(button)
    markup.row(button2)
    markup.row(button3, button4)
    bot.send_message(message.chat.id, 'fdfdfdfdf', reply_markup=markup)
    conn = sqlite3.connect('Clouth.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS wother(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Photo,
    Size varchar(20),
    Discription varchar(70),
    Type varchar(20)
    );""")
    conn.commit()
    cur.close()
    conn.close()

@bot.message_handler()
def message(message):
    global A
    if message.text == 'Смотреть одежду':
        button = types.KeyboardButton('Верх')
        button2 = types.KeyboardButton('Низ')
        button3 = types.KeyboardButton('Обувь')
        button4 = types.KeyboardButton('Аксессуары')
        button5 = types.KeyboardButton('Смотреть все')
        button6 = types.KeyboardButton('Назад')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
        markup.row(button6)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'Назад':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button7 = types.KeyboardButton('Смотреть одежду')
        button8 = types.KeyboardButton('Добавить одежду')
        button9 = types.KeyboardButton('Моя одежда')
        button10 = types.KeyboardButton('Корзина')
        markup2.row(button7)
        markup2.row(button8)
        markup2.row(button9, button10)
        bot.send_message(message.chat.id, 'dfdfdfdfdf', reply_markup=markup2)
    if message.text == 'Верх':
        button = types.KeyboardButton('Футболки')
        button2 = types.KeyboardButton('Свитшоты')
        button3 = types.KeyboardButton('Толстовки')
        button4 = types.KeyboardButton('Куртки')
        button6 = types.KeyboardButton('Смотреть несколько')
        button7 = types.KeyboardButton('Смотреть все')
        button8 = types.KeyboardButton('Назад.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button6)
        markup.row(button7)
        markup.row(button8)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'Низ':
        button = types.KeyboardButton('Джинсы')
        button2 = types.KeyboardButton('Брюки')
        button3 = types.KeyboardButton('Юбки')
        button4 = types.KeyboardButton('Шорты')
        button6 = types.KeyboardButton('Смотреть несколько')
        button7 = types.KeyboardButton('Смотреть все')
        button8 = types.KeyboardButton('Назад.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button6)
        markup.row(button7)
        markup.row(button8)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'Обувь':
        button = types.KeyboardButton('Кросовки')
        button2 = types.KeyboardButton('Кеды')
        button3 = types.KeyboardButton('Туфли')
        button4 = types.KeyboardButton('Босоножки')
        button5 = types.KeyboardButton('Сланцы')
        button6 = types.KeyboardButton('Смотреть несколько')
        button7 = types.KeyboardButton('Смотреть все')
        button8 = types.KeyboardButton('Назад.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
        markup.row(button6)
        markup.row(button7)
        markup.row(button8)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'Аксессуары':
        button = types.KeyboardButton('Сумки')
        button2 = types.KeyboardButton('Рюкзаки')
        button3 = types.KeyboardButton('Украшения')
        button4 = types.KeyboardButton('Ремни')
        button6 = types.KeyboardButton('Смотреть несколько')
        button7 = types.KeyboardButton('Смотреть все')
        button8 = types.KeyboardButton('Назад.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button6)
        markup.row(button7)
        markup.row(button8)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'Назад.':
        button = types.KeyboardButton('Верх')
        button2 = types.KeyboardButton('Низ')
        button3 = types.KeyboardButton('Обувь')
        button4 = types.KeyboardButton('Аксессуары')
        button5 = types.KeyboardButton('Смотреть все')
        button6 = types.KeyboardButton('Назад')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
        markup.row(button6)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'Добавить одежду':
        button = types.KeyboardButton('Главное меню')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button)
        bot.send_message(message.chat.id, 'Отправьте фотку', reply_markup= markup)
        bot.register_next_step_handler(message, Save)
    if message.text == 'Футболки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit1[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Футболки',))
        pool = cur.fetchall()
        if pool == []:
            limit1[idn] = 0
        nm = limit1[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Футболки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit1[idn] = limit1[idn] + 1
        vibor[idn] = 'Футболки'
        A = limit1
    if message.text == 'Свитшоты':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit2[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Свитшоты',))
        pool = cur.fetchall()
        if pool == []:
            limit2[idn] = 0
        nm = limit2[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Свитшоты',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit2[idn] = limit2[idn] + 1
        vibor[idn] = 'Свитшоты'
        A = limit2
    if message.text == 'Толстовки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit3[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Толстовки',))
        pool = cur.fetchall()
        if pool == []:
            limit3[idn] = 0
        nm = limit3[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Толстовки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit3[idn] = limit3[idn] + 1
        vibor[idn] = 'Толстовки'
        A = limit3
    if message.text == 'Куртки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit4[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Куртки',))
        pool = cur.fetchall()
        if pool == []:
            limit4[idn] = 0
        nm = limit4[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Куртки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit4[idn] = limit4[idn] + 1
        vibor[idn] = 'Куртки'
        A = limit4
    if message.text == 'Джинсы':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit5[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Джинсы',))
        pool = cur.fetchall()
        if pool == []:
            limit5[idn] = 0
        nm = limit5[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Джинсы',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit5[idn] = limit5[idn] + 1
        vibor[idn] = 'Джинсы'
        A = limit5
    if message.text == 'Брюки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit6[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Брюки',))
        pool = cur.fetchall()
        if pool == []:
            limit6[idn] = 0
        nm = limit6[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Брюки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit6[idn] = limit6[idn] + 1
        vibor[idn] = 'Брюки'
        A = limit6
    if message.text == 'Юбки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit7[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Юбки',))
        pool = cur.fetchall()
        if pool == []:
            limit7[idn] = 0
        nm = limit7[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Юбки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit7[idn] = limit7[idn] + 1
        vibor[idn] = 'Юбки'
        A = limit7
    if message.text == 'Шорты':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit8[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Шорты',))
        pool = cur.fetchall()
        if pool == []:
            limit8[idn] = 0
        nm = limit8[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Шорты',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit8[idn] = limit8[idn] + 1
        vibor[idn] = 'Шорты'
        A = limit8
    if message.text == 'Кросовки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit9[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Кросовки',))
        pool = cur.fetchall()
        if pool == []:
            limit9[idn] = 0
        nm = limit9[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Кросовки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup, parse_mode="html")
        cur.close()
        conn.close()
        limit9[idn] = limit9[idn] + 1
        vibor[idn] = 'Кросовки'
        A = limit9
    if message.text == 'Кеды':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit10[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Кеды',))
        pool = cur.fetchall()
        if pool == []:
            limit10[idn] = 0
        nm = limit10[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Кеды',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit10[idn] = limit10[idn] + 1
        vibor[idn] = 'Кеды'
        A = limit10
    if message.text == 'Туфли':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit11[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Туфли',))
        pool = cur.fetchall()
        if pool == []:
            limit11[idn] = 0
        nm = limit11[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Туфли',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit11[idn] = limit11[idn] + 1
        vibor[idn] = 'Туфли'
        A = limit11
    if message.text == 'Босоножки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit12[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Босоножки',))
        pool = cur.fetchall()
        if pool == []:
            limit12[idn] = 0
        nm = limit12[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Босоножки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit12[idn] = limit12[idn] + 1
        vibor[idn] = 'Босоножки'
        A = limit12
    if message.text == 'Сланцы':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit13[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Сланцы',))
        pool = cur.fetchall()
        if pool == []:
            limit13[idn] = 0
        nm = limit13[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Сланцы',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit13[idn] = limit13[idn] + 1
        vibor[idn] = 'Сланцы'
        A = limit13
    if message.text == 'Сумки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit14[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Сумки',))
        pool = cur.fetchall()
        if pool == []:
            limit14[idn] = 0
        nm = limit14[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Сумки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup, parse_mode="html")
        cur.close()
        conn.close()
        limit14[idn] = limit14[idn] + 1
        vibor[idn] = 'Сумки'
        A = limit14
    if message.text == 'Рюкзаки':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit15[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Рюкзаки',))
        pool = cur.fetchall()
        if pool == []:
            limit15[idn] = 0
        nm = limit15[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Рюкзаки',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit15[idn] = limit15[idn] + 1
        vibor[idn] = 'Рюкзаки'
        A = limit15
    if message.text == 'Украшения':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit16[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Украшения',))
        pool = cur.fetchall()
        if pool == []:
            limit16[idn] = 0
        nm = limit16[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Украшения',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit16[idn] = limit16[idn] + 1
        vibor[idn] = 'Украшения'
        A = limit16
    if message.text == 'Ремни':
        button = types.KeyboardButton('Меню')
        button2 = types.KeyboardButton('след')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = limit17[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Ремни',))
        pool = cur.fetchall()
        if pool == []:
            limit17[idn] = 0
        nm = limit17[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", ('Ремни',))
        pool = cur.fetchall()
        if pool == []:
            bot.send_message(message.chat.id, 'В данной категории нету товаров')
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info, reply_markup= markup)
        cur.close()
        conn.close()
        limit17[idn] = limit17[idn] + 1
        vibor[idn] = 'Ремни'
        A = limit17
    if message.text == 'Меню':
        button = types.KeyboardButton('Верх')
        button2 = types.KeyboardButton('Низ')
        button3 = types.KeyboardButton('Обувь')
        button4 = types.KeyboardButton('Аксессуары')
        button5 = types.KeyboardButton('Смотреть все')
        button6 = types.KeyboardButton('Назад')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
        markup.row(button6)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    if message.text == 'след':
        conn = sqlite3.connect('Clouth.db')
        cur = conn.cursor()
        idn = message.chat.id
        nm = A[idn] 
        vi = vibor[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", (f'{vi}',))
        pool = cur.fetchall()
        if pool == []:
            A[idn] = 0
        nm = A[idn]
        cur.execute(f"SELECT Photo, Size, Discription FROM wother WHERE Type = ? limit 1 offset {nm}", (f'{vi}',))
        pool = cur.fetchall()
        for el in pool:
            photo = el[0]
            info = f'Size:{el[1]}\nОписание: {el[2]}'
            sendPhoto = open(f'photos/{photo}', 'br')
            bot.send_photo(message.chat.id, sendPhoto, info)
            cur.close()
            conn.close()
            A[idn] = A[idn] + 1





bot.polling(none_stop=True)