import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('ййййй')

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Привет' or message.text == 'Йоу' or message.text == 'привет' or message.text == 'йоу':
        bot.send_message(message.from_user.id, "Здравствуй, хочешь подготовться к какому нибудь предмету?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши Йоу')


def get_name(message):
    global name
    name = message.text
    if name == 'Не' or name == 'Нет' or name == 'нет' or name == 'Да' or name == 'да':
        bot.send_message(message.from_user.id, 'Ну судьба несправедлива, готовы к страданиям во имя будущего?')
        bot.register_next_step_handler(message, get_age)


def get_age(message):
    keyboard = types.InlineKeyboardMarkup()
    key_o = types.InlineKeyboardButton(text='Подготовка к русскому',
                                       callback_data='q')
    keyboard.add(key_o)
    ke_yes = types.InlineKeyboardButton(text='Подготовка к информатике', callback_data='w')
    keyboard.add(ke_yes)
    key_o = types.InlineKeyboardButton(text='Подготовка к математике',
                                       callback_data='e')
    keyboard.add(key_o)
    key_yes = types.InlineKeyboardButton(text='Подготовка к физике', callback_data='r')
    keyboard.add(key_yes)
    key_o = types.InlineKeyboardButton(text='Подготовка к химии',
                                       callback_data='t')
    keyboard.add(key_o)
    key_o = types.InlineKeyboardButton(text='Подготовка к географии',
                                       callback_data='y')
    keyboard.add(key_o)

    key_ys = types.InlineKeyboardButton(text='Успокаивающая музыка',
                                        callback_data='u')
    keyboard.add(key_ys)

    question = 'Выберите тему, которая вас интересует'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "q":
        bot.send_message(call.message.chat.id, '1')

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='qq')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='ww')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='ee')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='rr')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='tt')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    elif call.data == "w":
        bot.send_message(call.message.chat.id, '2')
    elif call.data == "e":
        bot.send_message(call.message.chat.id, '3')
    elif call.data == "r":
        bot.send_message(call.message.chat.id, '4')
    elif call.data == "t":
        bot.send_message(call.message.chat.id, '5')
    elif call.data == "y":
        bot.send_message(call.message.chat.id, '6')
    elif call.data == "u":
        bot.send_message(call.message.chat.id, '7')

    if call.data == "qq":
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor1 FROM oge AS f WHERE f.id = 'Русский язык' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)

    if call.data == "ww":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/GzdTLnn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/1XVdiB4')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/q4uYBxZ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fsIfdqX')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/7BikPg2')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/lzDbeSZ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wnerAmd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/RXzabuW')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZiN4ZNa')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/0VunlaB')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/N01WTx0')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Y4koZIk')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/c6CR8z3')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/HDUqCz5')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/g2UCOQb')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/pjxVFOG')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/hQHMSQl')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/9bced9t')

    if call.data == "tt":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')


bot.polling(none_stop=True, interval=0)
