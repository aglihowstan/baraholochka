import telebot
from telebot import types
from keys import BOT_API_KEYgit 

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
    bot.send_message(message.chat.id, welcome, reply_markup=markup)

@bot.message_handler()
def message(message):
    if message.text == 'Смотреть одежду':
        button = types.KeyboardButton('Верх')
        button2 = types.KeyboardButton('Низ')
        button3 = types.KeyboardButton('Обувь')
        button4 = types.KeyboardButton('Аксессуары')
        button5 = types.KeyboardButton('Смотреть все')
        markup = types.ReplyKeyboardMarkup()
        markup.row(button, button2)
        markup.row(button3, button4)
        markup.row(button5)
        bot.send_message(message.chat.id, "Выберите, что хотите посмотреть", reply_markup=markup)
    elif message.text == 'Добавить одежду':
        pass
    elif message.text == 'Моя одежда':
        pass
    elif message.text == 'Корзина':
        pass
    else:
        bot.send_message(message.chat.id, "Нет данного выбора")


bot.polling(none_stop=True)