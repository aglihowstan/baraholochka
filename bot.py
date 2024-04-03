import telebot
from telebot import types
from keys import BOT_API_KEY

bot = telebot.TeleBot(BOT_API_KEY)
welcome = open('textes/welcome.txt', 'rb')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Смотреть одежду')
    button2 = types.KeyboardButton('Добавить одежду')
    button3 = types.KeyboardButton('Моя одежда')
    button4 = types.KeyboardButton('Корзина')
    markup.row(button)
    markup.row(button2)
    markup.row(button3, button4)
    bot.send_message(message.chat.id, 'fdfdfdfdf', reply_markup=markup)

@bot.message_handler()
def message(message):
    if message.text == 'Смотреть одежду':
        button = types.KeyboardButton('Верх')
        button2 = types.KeyboardButton('Низ')
        button3 = types.KeyboardButton('Обувь')
        button4 = types.KeyboardButton('Аксессуары')
        button5 = types.KeyboardButton('Смотреть все')
        button6 = types.KeyboardButton('Назад')
        markup = types.ReplyKeyboardMarkup()
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
    if message.text == 'Добавить одежду':
        pass
    if message.text == 'Привет' :
        pass
    if message.text == 'Моя одежда':
        pass
    if message.text == 'Обувь':
        button = types.KeyboardButton('Кросовки')
        button2 = types.KeyboardButton('Кеды')
        button3 = types.KeyboardButton('Туфли')
        button4 = types.KeyboardButton('Босоножки')
        button5 = types.KeyboardButton('Сланцы')
        button6 = types.KeyboardButton('Смотреть несколько')
        button7 = types.KeyboardButton('Смотреть все')
        button8 = types.KeyboardButton('Назад.')
        markup = types.ReplyKeyboardMarkup()
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
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
        markup = types.ReplyKeyboardMarkup()
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
        markup.row(button6)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)





bot.polling(none_stop=True)