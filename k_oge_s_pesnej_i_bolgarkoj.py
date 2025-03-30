import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('йййй')

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
        bot.send_message(message.from_user.id, 'Вы гоовы грызть гранит науки?')
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
        bot.send_message(call.message.chat.id, '1')

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

    if call.data == "t":
        bot.send_message(call.message.chat.id, '1')

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
        key_o = types.InlineKeyboardButton(text='Задание 14',
                                           callback_data='g1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Задание 15',
                                           callback_data='h1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 16',
                                           callback_data='j1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 17',
                                           callback_data='k1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 18',
                                           callback_data='z1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 19',
                                           callback_data='x1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 20',
                                           callback_data='c1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 21',
                                           callback_data='v1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 22',
                                           callback_data='b1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 23',
                                           callback_data='n1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 24',
                                           callback_data='m1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 25',
                                           callback_data='mq1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 26',
                                           callback_data='mw1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 27',
                                           callback_data='me1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 28',
                                           callback_data='mr1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 29',
                                           callback_data='mt1')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Задание 30',
                                           callback_data='my1')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='t6')
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

    if call.data == "m5":
        bot.send_message(call.message.chat.id, 'https://chem-oge.sdamgia.ru/')

    if call.data == "q6":
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor3 FROM oge AS f WHERE f.id = 'Русский язык' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)

    if call.data == "t6":
        bot.send_message(call.message.chat.id, 'https://geo-oge.sdamgia.ru/')


bot.polling(none_stop=True, interval=0)
