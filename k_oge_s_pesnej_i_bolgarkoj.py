import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('7456789')

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Привет' or message.text == 'Йоу' or message.text == 'привет' or message.text == 'йоу':
        bot.send_message(message.from_user.id, "Здравствуй, хочешь подготовться к какому нибудь предмету?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'Распили меня болгаркой':
        bot.reply_to(message, 'Мне нравится твой энтузиазм, но для этого не время')
        bot.send_message(message.from_user.id, 'Хотя.....')
        bot.send_message(message.from_user.id, 'ВРУМ ВРУМ ВРУМ ВРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР')
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'Похорони меня за плинтусом':
        bot.reply_to(message, 'Прости, но мы его уже второй год не можем приклеить, так что иди учись')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши Йоу')


def get_name(message):
    global name
    name = message.text
    if name == 'Не' or name == 'Нет' or name == 'нет':
        bot.send_message(message.from_user.id, 'Ну судьба несправедлива, готовы к страданиям во имя будущего?')
        bot.register_next_step_handler(message, get_age)

    elif name == 'Да' or name == 'да':
        bot.send_message(message.from_user.id, 'Вы готовы грызть гранит науки?')
        bot.register_next_step_handler(message, get_age)

    elif name == 'Распили меня болгаркой':
        bot.reply_to(message, 'Мне нравится твой энтузиазм, но для этого не время')
        bot.send_message(message.from_user.id, 'Хотя.....')
        bot.send_message(message.from_user.id, 'ВРУМ ВРУМ ВРУМ ВРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР')
        bot.register_next_step_handler(message, get_age)

    elif name == 'Похорони меня за плинтусом':
        bot.reply_to(message, 'Прости, но мы его уже второй год не можем приклеить, так что иди учись')
    else:
        bot.send_message(message.from_user.id, 'Я твое бу бу бу не понимаю, катись заниматься')
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
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='q1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='w1')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='e1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='r1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 5',
                                           callback_data='t1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 6',
                                           callback_data='y1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 7',
                                           callback_data='u1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 8',
                                           callback_data='i1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 9',
                                           callback_data='p1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 10',
                                           callback_data='a1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 11',
                                           callback_data='s1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 12',
                                           callback_data='d1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 13',
                                           callback_data='f1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='g1')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "w":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='q2')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='w2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='e2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='r2')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 5',
                                           callback_data='t2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 6',
                                           callback_data='y2')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 7',
                                           callback_data='u2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 8',
                                           callback_data='i2')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 9',
                                           callback_data='p2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 10',
                                           callback_data='a2')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 11',
                                           callback_data='s2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 12',
                                           callback_data='d2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 13',
                                           callback_data='f2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 14',
                                           callback_data='g2')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 15',
                                           callback_data='h2')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 16',
                                           callback_data='j2')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='k2')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "e":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='q3')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='w3')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='e3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='r3')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 5',
                                           callback_data='t3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 6',
                                           callback_data='y3')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 7',
                                           callback_data='u3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 8',
                                           callback_data='i3')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 9',
                                           callback_data='p3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 10',
                                           callback_data='a3')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 11',
                                           callback_data='s3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 12',
                                           callback_data='d3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 13',
                                           callback_data='f3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 14',
                                           callback_data='g3')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 15',
                                           callback_data='h3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 16',
                                           callback_data='j3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 17',
                                           callback_data='k3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 18',
                                           callback_data='z3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 19',
                                           callback_data='x3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 20',
                                           callback_data='c3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 21',
                                           callback_data='v3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 22',
                                           callback_data='b3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 23',
                                           callback_data='n3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 24',
                                           callback_data='m3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 25',
                                           callback_data='mq3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='mw3')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "r":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='q4')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='w4')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='e4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='r4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 5',
                                           callback_data='t4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 6',
                                           callback_data='y4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 7',
                                           callback_data='u4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 8',
                                           callback_data='i4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 9',
                                           callback_data='p4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 10',
                                           callback_data='a4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 11',
                                           callback_data='s4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 12',
                                           callback_data='d4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 13',
                                           callback_data='f4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 14',
                                           callback_data='g4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 15',
                                           callback_data='h4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 16',
                                           callback_data='j4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 17',
                                           callback_data='k4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 18',
                                           callback_data='z4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 19',
                                           callback_data='x4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 20',
                                           callback_data='c4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 21',
                                           callback_data='v4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 22',
                                           callback_data='b4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='n4')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "t":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='q5')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='w5')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='e5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='r5')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 5',
                                           callback_data='t5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 6',
                                           callback_data='y5')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 7',
                                           callback_data='u5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 8',
                                           callback_data='i5')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 9',
                                           callback_data='p5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 10',
                                           callback_data='a5')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 11',
                                           callback_data='s5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 12',
                                           callback_data='d5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 13',
                                           callback_data='f5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 14',
                                           callback_data='g5')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 15',
                                           callback_data='h5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 16',
                                           callback_data='j5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 17',
                                           callback_data='k5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 18',
                                           callback_data='z5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 19',
                                           callback_data='x5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 20',
                                           callback_data='c5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 21',
                                           callback_data='v5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 22',
                                           callback_data='b5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 23',
                                           callback_data='n5')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='m5')
        keyboard.add(key_o)

        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "y":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Задание 1', callback_data='q6')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Задание 2', callback_data='w6')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Задание 3',
                                           callback_data='e6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 4',
                                           callback_data='r6')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 5',
                                           callback_data='t6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 6',
                                           callback_data='y6')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 7',
                                           callback_data='u6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 8',
                                           callback_data='i6')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 9',
                                           callback_data='p6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 10',
                                           callback_data='a6')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 11',
                                           callback_data='s6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 12',
                                           callback_data='d6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 13',
                                           callback_data='f6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 14',
                                           callback_data='g6')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 15',
                                           callback_data='h6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 16',
                                           callback_data='j6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 17',
                                           callback_data='k6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 18',
                                           callback_data='z6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 19',
                                           callback_data='x6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 20',
                                           callback_data='c6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 21',
                                           callback_data='v6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 22',
                                           callback_data='b6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 23',
                                           callback_data='n6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 24',
                                           callback_data='m6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 25',
                                           callback_data='mq6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 26',
                                           callback_data='mw6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 27',
                                           callback_data='me6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 28',
                                           callback_data='mr6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 29',
                                           callback_data='mt6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 30',
                                           callback_data='my6')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='mu6')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "u":
        audio = open('C:/Users/Andrey/Desktop/AB-.mp3', 'rb')
        bot.send_audio(call.from_user.id, audio)
        audio.close()

    if call.data == "q1":
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor1 FROM oge AS f WHERE f.id = 'Русский язык' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)

    if call.data == "w1":
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

    if call.data == "e1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/WV1unoH')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/d0cotb3')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/24gb8TX')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/4ADLZY6')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/KOXHyHt')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/XFPSzGH')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/hO4I6ex')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/FbYBckg')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/1JXN5uh')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/sF3oz7r')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/jcs2qs6')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/XZt2dQY')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/8vLotEz')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/3KXSpKV')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/U1OOL0d')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/BSsNi9x')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/xgTyUs5')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PX7g7w7')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/tcZDLCL')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/8bHqo1d')

    if call.data == "g1":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')

    if call.data == "q2":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')
    if call.data == "k2":
        bot.send_message(call.message.chat.id, 'https://inf-oge.sdamgia.ru/')

    if call.data == "q3":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')
    if call.data == "mw3":
        bot.send_message(call.message.chat.id, 'https://math-oge.sdamgia.ru/')

    if call.data == "q4":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')
    if call.data == "n4":
        bot.send_message(call.message.chat.id, 'https://phys-oge.sdamgia.ru/')

    if call.data == "q5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/dp0BWGC')

    if call.data == "w5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/anW2MLM')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/lquihjl')

    if call.data == "e5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZhA0wok')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/dxlvKu4')

    if call.data == "r5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Fo7ydKH')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/6GrV59M')

    if call.data == "t5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/oLevzuT')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/jKJbUHN')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/tX9pKbW')

    if call.data == "y5":
        bot.send_message(call.message.chat.id, 'В 6 задании обобщение всех материалов с 1 по 5.')

    if call.data == "u5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/6YaHc5V')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/cNN9NFY')

    if call.data == "i5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/dlkkDXh')

    if call.data == "p5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PQP137J')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Hy3Iqua')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/GKhpszg')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Ge0yZtY')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5Z1iSCA')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/eIZm0Lt')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JwOoBnD')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SDfEVg2')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5xf5U0g')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rUd2rlK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/KcLlWvX')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/k1733VZ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Ua6O8ik')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Wrp5Ut4')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/3bmE2lH')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fbZ4kjp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/kC4H8Im')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/YJZbHTO')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/4DO0h5w')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TxfSSGt')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/dLVmpvf')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nxgrMJ5')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wc6iVpp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rktXFST')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/0YKERYA')

    if call.data == "a5":
        bot.send_message(call.message.chat.id, 'Теория 9 и 10 задания взаимосвязана')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PQP137J')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Hy3Iqua')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/GKhpszg')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Ge0yZtY')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5Z1iSCA')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/eIZm0Lt')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JwOoBnD')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SDfEVg2')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5xf5U0g')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rUd2rlK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/KcLlWvX')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/k1733VZ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Ua6O8ik')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Wrp5Ut4')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/3bmE2lH')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fbZ4kjp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/kC4H8Im')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/YJZbHTO')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/4DO0h5w')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TxfSSGt')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/dLVmpvf')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nxgrMJ5')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wc6iVpp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rktXFST')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/0YKERYA')

    if call.data == "s5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JxxXEFp')
    if call.data == "d5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/0vLNThV')
    if call.data == "f5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/c5hz23z')
    if call.data == "g5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/T2b3nC3')
    if call.data == "h5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/vGXqmDz')
    if call.data == "j5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Z5cSQbk')

    if call.data == "m5":
        bot.send_message(call.message.chat.id, 'https://chem-oge.sdamgia.ru/')

    if call.data == "q6":
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor1 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)
    if call.data == "w6":
        bot.send_message(call.message.chat.id,
                         'Страны, граничащие с Россией: Норвегия, Финляндия, Эстония, Латвия, Литва, Польша,'
                         ' Белоруссия, Украина, Грузия, Азербайджан, Казахстан, КНР (Китай), Монголией, КНДР (Корея),'
                         ' Абхазия, Южная Осетия, по морю - Япония и США')
    if call.data == "e6":
        bot.send_message(call.message.chat.id,
                         'Природные и антропогенные причины возникновения геоэкологических проблем; меры'
                         ' по защите людей от стихийных природных явлений. Заповедники.')

    if call.data == "r6":
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor4 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)
    if call.data == "t6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZEGHn1F')
    if call.data == "y6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/P294DIf')

    if call.data == "u6":
        bot.send_message(call.message.chat.id, 'Чем выше слои горных пород тем моложе Самый молодой выше всех-наверху,'
                                               ' самый древний ниже всех внизу. Смотрим и обозначаем сверху вниз.')
    if call.data == "i6":
        bot.send_message(call.message.chat.id,
                         'Измеряем линейкой расстояние между объектами, потом умножаем на величину'
                         ' масштаба (например 100 м) 4 см х 100 = 400 м')
    if call.data == "p6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/WvlzJg9')
    if call.data == "a6":
        bot.send_message(call.message.chat.id, 'Определить можно по высоте точек, понижению рельефа и тд ')
    if call.data == "s6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/hO35O6T')
    if call.data == "d6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TDopsh6')
    if call.data == "f6":
        bot.send_message(call.message.chat.id, 'Знание карты местности')
    if call.data == "g6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5gcN57Q')
    if call.data == "h6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/LyYr8nY')
    if call.data == "j6":
        bot.send_message(call.message.chat.id, 'Анализ таблицы')
    if call.data == "k6":
        bot.send_message(call.message.chat.id, 'Чем восточнее, тем раньше встает солнце')
    if call.data == "z6":
        bot.send_message(call.message.chat.id, 'Если график температуры идет вверх, то это северное полушарие, '
                                               'а если вниз - южное')
    if call.data == "x6":
        bot.send_message(call.message.chat.id, 'Смотрите административную карту. Новый год '
                                               'начинается с востока и идет на запад')
    if call.data == "c6":
        bot.send_message(call.message.chat.id, 'Нужны карта мира: физическая, природных зон, политическая')

    if call.data == "v6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/YgmeKpP')
    if call.data == "b6":
        bot.send_message(call.message.chat.id, 'Определить по графику, таблице нужно величину')
    if call.data == "n6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZvpRLm6')
    if call.data == "m6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/acaxAAV')
    if call.data == "mq6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Z0CsKQJ')
    if call.data == "mw6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SV835gN')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fmHwzB6')
    if call.data == "me6":
        bot.send_message(call.message.chat.id, 'Карты административная и экономическое районирование')
    if call.data == "mr6":
        bot.send_message(call.message.chat.id, 'Карты физическая и экономическое районирование')

    if call.data == "mt6":
        bot.send_message(call.message.chat.id, 'Экономическое районирование')
    if call.data == "my6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/kbJVySr')
    if call.data == "mu6":
        bot.send_message(call.message.chat.id, 'https://geo-oge.sdamgia.ru/')


bot.polling(none_stop=True, interval=0)
