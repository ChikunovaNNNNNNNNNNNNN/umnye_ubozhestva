import telebot
from telebot import types
import sqlite3
from random import choice

bot = telebot.TeleBot('7654642510:AAEU9dj-4OT4CgIlTbPrhp6aahxRvZygtXc')

name = ''
surname = ''
age = 0
musics = ['AB-.mp3', 'Ophelia - The Lumineers', 'Riptide - Vance Joy', 'Stolen Dance - Milky Chance',
          "There's Nothing Holdin' Me Back - Shawn Mendes", 'Build Our Machine (Bendy and Ink Machine)']


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

    key_o = types.InlineKeyboardButton(text='Подготовка к история',
                                       callback_data='hist')
    keyboard.add(key_o)

    key_o = types.InlineKeyboardButton(text='Подготовка к литература',
                                       callback_data='lit')
    keyboard.add(key_o)

    key_o = types.InlineKeyboardButton(text='Подготовка к обществознание',
                                       callback_data='obch')
    keyboard.add(key_o)

    key_o = types.InlineKeyboardButton(text='Подготовка к биологии',
                                       callback_data='bio')
    keyboard.add(key_o)

    key_o = types.InlineKeyboardButton(text='Подготовка к иностранным языкам',
                                       callback_data='lang')
    keyboard.add(key_o)

    key_ys = types.InlineKeyboardButton(text='Успокаивающая музыка',
                                        callback_data='u')
    keyboard.add(key_ys)

    kqqq_ys = types.InlineKeyboardButton(text='Даты проведения экзаменов',
                                         callback_data='dat')
    keyboard.add(kqqq_ys)

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

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='g2')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "e":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Теория по алгебре', callback_data='alg')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Теория по геометрии', callback_data='geom')
        keyboard.add(ke_yes)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='mw3')
        keyboard.add(key_o)
        question = 'Выберите задание'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "alg":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Формулы сокращенного умножения.', callback_data='q3')
        keyboard.add(key_yes)
        ke_yes = types.InlineKeyboardButton(text='Арифметический квадратный корень.', callback_data='w3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Арифметическая прогрессия.', callback_data='e3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Геометрическая прогрессия.', callback_data='r3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Классическое определение вероятности.', callback_data='t3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Текстовые задачи на среднюю скорость.', callback_data='y3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Текстовые задачи на нахождение длины поезда.', callback_data='u3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Текстовые задачи на проценты, смеси и сплавы.', callback_data='i3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Текстовые задачи на движение по воде.', callback_data='p3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Текстовые задачи на совместную работу.', callback_data='a3')
        keyboard.add(ke_yes)
        question = 'Выберите тему для подготовки по алгебре'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "geom":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Взаимное расположение прямых на плоскости.', callback_data='s3')
        keyboard.add(key_yes)
        ke_yes = types.InlineKeyboardButton(text='Треугольник.', callback_data='d3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Теорема Пифагора.', callback_data='f3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Теорема Фалеса и теорема о пропорциональных отрезках.',
                                            callback_data='g3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Вневписанная окружность треугольника.', callback_data='h3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Параллелограмм.', callback_data='j3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Трапеция.', callback_data='k3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Свойства и признаки вписанного четырехугольника.', callback_data='z3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Свойства и признаки описанного четырехугольника.', callback_data='x3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Теорема Птолемея.', callback_data='c3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Углы, связанные с окружностью.', callback_data='v3')
        keyboard.add(ke_yes)

        ke_yes = types.InlineKeyboardButton(text='Метрические соотношения в окружности.', callback_data='b3')
        keyboard.add(ke_yes)
        ke_yes = types.InlineKeyboardButton(text='Векторы и координаты на плоскости.', callback_data='n3')
        keyboard.add(ke_yes)

        question = 'Выберите тему для подготовки по геометрии'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "r":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Механические явления', callback_data='q4')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Тепловые явления', callback_data='w4')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Электромагнитные явления',
                                           callback_data='e4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Квантовые явления. Работа с текстами физического содержания',
                                           callback_data='r4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Экспериментальное задание. Методология науки. Приборы и технические '
                                                'устройства. История физики',
                                           callback_data='t4')
        keyboard.add(key_o)

        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='u4')
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

    if call.data == "dat":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Досрочный период', callback_data='dat1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Основной период', callback_data='dat2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Дополнительный период',
                                           callback_data='dat3')
        keyboard.add(key_o)
        question = 'Выберите период'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)

    if call.data == "u":
        audio = open('C:/Users/Andrey/Desktop/AB-.mp3', 'rb')
        bot.send_audio(call.from_user.id, audio)
        audio.close()
        bot.send_message(call.message.chat.id, 'https://disk.yandex.ru/d/SkNedXrjj4qavw')

    if call.data == "q1":
        con = sqlite3.connect('1.sqlite')
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
    if call.data == "r1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/bhXrPLJ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/gL1LZti')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/mwTzPXd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/R4NUnOS')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/pbB703R')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/gea3E06')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/1xcZ06G')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/NnLTXAa')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5evSo4l')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ObgHLQI')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/UG7PQBd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PiXEMV0')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/DjH34TG')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/YDeb0hR')

        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/eQhhInA')
    if call.data == "t1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/lTJ5fzq')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/woFFylL')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TwjMIIb')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/gBn4Nej')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nyk2sCN')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ztrAR0O')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Sts5VhF')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/LO1VYkA')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/6YZNIDQ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Nj3UfBi')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/qedn1mE')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/8PZexPs')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PicRZgC')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/iJiZPND')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rJllZAJ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/EoxRAS7')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/INVEFSk')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/eKxNckK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fHVMMl4')
    if call.data == "y1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/L0JFhs2')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/RR1jjPn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/s9yPCGl')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SKcbKc8')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SDc5dCO')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/v0dqQ3b')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Lj05rkG')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SUqHV9q')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/lRhSMzV')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5ctGUjB')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Bj7oLCn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fg8EF8F')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/F5KmhJS')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ht2LayY')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/QFxxyr1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/whraVrM')
    if call.data == "u1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ldc1gfm')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/mxBAjzL')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/4UtnPqE')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/HdExlP5')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/xpoTb9w')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/DwlRl13')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/l3uHhV9')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/SwQbrxZ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rJw3Q5h')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/QHbAew5')

    if call.data == "i1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fGfeXKM')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JfMWG3Y')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/w5LPPex')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/WX2EQ2n')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/9wVqizj')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/jqOHQeV')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wKYkr5G')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wbZcDzu')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Kni6iec')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JoGB7zM')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/y5A37VS')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ahEajVW')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/xg8ujlK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/0SajnIz')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/HCy1PRy')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/IHL12ev')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/km60f4q')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/NKOamco')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wrettus')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZFYQcSn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/HUgREbK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/4US5CPf')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/2agKqmM')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/y5SmpKm')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Xd61Pwh')
    if call.data == "p1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/HYxGtpp')
    if call.data == "a1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JUqkDkp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Vf4xdgQ')
    if call.data == "s1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/bVHZmkn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5EKUiTF')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/AJiBqO7')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/sdkhUHX')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ibu0g8E')

    if call.data == "d1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/0P6vPCZ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/5pRWFts')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/S0Z9udw')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TDgImZ5')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/VVAqIQ1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZBXfNBn')
    if call.data == "f1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/omyxfd8')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/kdNnr74')

    if call.data == "h1":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')

    if call.data == "q2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/x81E5hS')
    if call.data == "w2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ElPdZqd')
    if call.data == "e2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/a0jzuXP')
    if call.data == "r2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PSZhnU7')
    if call.data == "t2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/H85FFOm')
    if call.data == "y2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/2dZH1OQ')
    if call.data == "u2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TJwmTv4')
    if call.data == "i2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/HzD7ALt')
    if call.data == "p2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/cwWQYhy')
    if call.data == "a2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/xQbudY2')
    if call.data == "s2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/POmCrVp')
    if call.data == "d2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nmULMWG')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/NzgCTy9')
    if call.data == "f2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nmULMWG')

    if call.data == "g2":
        bot.send_message(call.message.chat.id, 'https://inf-oge.sdamgia.ru/')

    if call.data == "q3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/zm6AeUW')
    if call.data == "w3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/6yMxOQY')
    if call.data == "e3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fZuCSlf')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/fqCmIQl')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/eUwxnv3')
    if call.data == "r3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/7eeBQz0')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/yFOkVjr')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/FcQCHVC')
    if call.data == "t3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/bTQQy7g')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/yFOkVjr')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/FcQCHVC')
        'veroyatnost'
    if call.data == "y3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/iPfLHNd')
    if call.data == "u3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/MtMMXxY')
    if call.data == "i3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/YNqPxj1')
    if call.data == "p3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TdPAZRh')
    if call.data == "a3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/iDg9Jy6')

    if call.data == "s3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/8Uqg9pd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/AyGO0s0')
    if call.data == "d3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/zNuhqaQ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/vjWYbuY')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/NYUIV5N')
    if call.data == "f3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/jHkeTal')
    if call.data == "g3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/eVLl8zx')
    if call.data == "h3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/gwtrliL')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/cXKwgls')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/oeilfiV')
    if call.data == "j3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZPRiH4u')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ulpcjop')
    if call.data == "k3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nEj9Nks')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/EjzRxOI')
    if call.data == "z3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/nB5WVJO')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PUV4kN1')
    if call.data == "x3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/GEmnoIg')
    if call.data == "c3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/YCmiPka')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/47OURU5')
    if call.data == "v3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/UadvDW9')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/8drmNkE')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wGqwH02')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ACVRZ4y')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/rK5gPIP')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/LNHGNhr')
    if call.data == "b3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/TrBO1KY')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/DM9pW8L')
    if call.data == "n3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/O1eFk6G')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/NUQPHo7')
    if call.data == "mw3":
        bot.send_message(call.message.chat.id, 'https://math-oge.sdamgia.ru/')

    if call.data == "q4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/zMfFuA9')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/LDkGdtP')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/WuBwcvJ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/JntwPga')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/yCyvuFA')
    if call.data == "w4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/KAgAgHt')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/pE63T3j')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ePsf8x4')
    if call.data == "e4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/3T0cgmP')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/wr9ZC2e')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/hyu2FLl')
    if call.data == "r4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/xESocsa')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/Pfa6nwd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/O9JeOFk')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/7OOfPFI')
    if call.data == "t4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/XnNkifC')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/ZBBelb1')
    if call.data == "u4":
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
    if call.data == "k5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/LRlBS8f')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/FNWHzoW')
    if call.data == "z5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PgxuLpL')
    if call.data == "x5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/PgxuLpL')
    if call.data == "c5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/1DclIuK')

    if call.data == "v5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/vt2Vbxq')
    if call.data == "b5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/XQDzt0j')
    if call.data == "n5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/XQDzt0j')
    if call.data == "m5":
        bot.send_message(call.message.chat.id, 'https://chem-oge.sdamgia.ru/')

    if call.data == "q6":
        con = sqlite3.connect('1.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor1 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)
    if call.data == "w6":
        con = sqlite3.connect('1.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor2 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)
    if call.data == "e6":
        con = sqlite3.connect('1.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor3 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)

    if call.data == "r6":
        con = sqlite3.connect('1.sqlite')
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
        con = sqlite3.connect('1.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor7 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        print(*res[0])
        bot.send_message(call.message.chat.id, *res)
    if call.data == "i6":
        con = sqlite3.connect('1.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor8 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        con.close()
        bot.send_message(call.message.chat.id, *res)
    if call.data == "p6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/a/WvlzJg9')
    if call.data == "a6":
        con = sqlite3.connect('1.sqlite')
        cur = con.cursor()
        qwq = """ SELECT f.teor10 FROM oge AS f WHERE f.id = 'География' """
        res = cur.execute(qwq).fetchall()
        bot.send_message(call.message.chat.id, *res)
        con.close()
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
    if call.data == "g1":
        bot.send_message(call.message.chat.id, 'https://rus-oge.sdamgia.ru/')
    if call.data == "lit":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Древнерусская литература и литература XVIII века',
                                             callback_data='lit1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Русская литература первой половины XIX века', callback_data='lit2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Литература второй половины XIX века',
                                           callback_data='lit3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Литература XX в. – начала XXI века',
                                           callback_data='lit4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='lit5')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "lit1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/eFOWhle')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/vwnSH5P')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/WHxWC0I')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/TuIs7eG')
    if call.data == "lit2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/7Uk3Bt2')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/Jx4Mt9R')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/dG7GWSJ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/qvjvvxK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/z4LyaZ0')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/daMkeGa')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/LCw0Zj0')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/A7xJdsq')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/QwituH0')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/HcalCx9')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/nxq2V5I')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/54tpCcK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/vW1wi8x')
    if call.data == "lit3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/X3c2CLb')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/XXdVTvb')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/xtVBuJl')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/6DzLB7l')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/LFmErah')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/KwYdnKQ')
    if call.data == "lit4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/b0kkAjd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/0Gcx50w')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/mPoVTHA')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/uhW4axq')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/u3GE2qb')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/ay0D9dF')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/rVHZBlA')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/xvNzWqU')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/t4K6QqP')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/sw4T4w0')
    if call.data == "lit5":
        bot.send_message(call.message.chat.id, 'https://lit-oge.sdamgia.ru/')
    if call.data == "hist":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(
            text='История России с древнейших времён до начала XVI в. История Древнего '
                 'мира. История Средних веков', callback_data='hist1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='История России в 1505 – 1682 гг. История зарубежных стран в новое '
                                                 'время (XVI – XVII вв.)', callback_data='hist2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text=' История России с 1682 до 1801 г. История зарубежных стран в новое'
                                                ' время (XVIII в.)', callback_data='hist3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='История России с 1801 по 1914 г. Новая история зарубежных стран в '
                                                'XIX – начале XX в.', callback_data='hist4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Всеобщая история с древнейших времен до 1914 г.',
                                           callback_data='hist5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='hist6')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "hist1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/YhXno4I')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/En8FgB1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/8iq7lgu')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/bXHlQx4')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/jg4oIRb')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/1EYHIZh')
    if call.data == "hist2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/8dS52df')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/ib4PdHx')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/xz5ooSa')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/Gj9ridL')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/AnL2Yw1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/VjghFSp')
    if call.data == "hist3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/VyOqXP7')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/eu0eroj')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/eoiI6Pu')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/iYGOY8v')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/2Ok5uKs')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/DRcZRxK')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/YaQfTGQ')
    if call.data == "hist4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/iitid6N')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/QN7Bqe4')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/LPeuFde')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/YflmGVG')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/Q8d49G2')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/qXBXNW7')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/l1vxawj')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/fVPbhQW')
    if call.data == "hist5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/sbEuXBn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/dqKwkkp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/bYLf0n1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/rQzrIvx')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/9cYam6n')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/XsyTrvq')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/SwZMZjo')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/cUPS0fJ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/RMftbUp')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/G9O6Dbx')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/oEdsbak')
    if call.data == "hist6":
        bot.send_message(call.message.chat.id, 'https://hist-oge.sdamgia.ru/')
    if call.data == "lang":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Французский', callback_data='fr')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Английский', callback_data='en')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Немецкий',
                                           callback_data='deu')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Испанский',
                                           callback_data='sp')
        keyboard.add(key_o)
        question = 'Выберите язык'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "fr":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Аудирование', callback_data='fr1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Чтение', callback_data='fr2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Лекс-грамм',
                                           callback_data='fr3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Письмо',
                                           callback_data='fr4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Говорение',
                                           callback_data='fr5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='fr6')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "fr1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/JGAqAqm')
    if call.data == "fr2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/47YItW0')
    if call.data == "fr3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/iGiktGa')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/ghPkt8T')
    if call.data == "fr4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/FLNtGR2')
    if call.data == "fr5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/NGWi6XO')
    if call.data == "fr6":
        bot.send_message(call.message.chat.id, 'https://fr-oge.sdamgia.ru/')
    if call.data == "en":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Аудирование', callback_data='en1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Чтение', callback_data='en2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Лекс-грамм',
                                           callback_data='en3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Письмо',
                                           callback_data='en4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Говорение',
                                           callback_data='en5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='en6')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "en1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/YWC2YGA')
    if call.data == "en2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/DzIhY4l')
    if call.data == "en3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/BmsjALe')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/2SYROAj')
    if call.data == "en4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/Sbx1r6S')
    if call.data == "en5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/tWYuqO0')
    if call.data == "en6":
        bot.send_message(call.message.chat.id, 'https://en-oge.sdamgia.ru/')
    if call.data == "deu":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Аудирование', callback_data='deu1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Чтение', callback_data='deu2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Лекс-грамм',
                                           callback_data='deu3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Письмо',
                                           callback_data='deu4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Говорение',
                                           callback_data='deu5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='deu6')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "deu1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/XDtx2OP')
    if call.data == "deu2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/XtO57jG')
    if call.data == "deu3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/amxmX58')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/UOG4sH6')
    if call.data == "deu4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/lQH0Hfd')
    if call.data == "deu5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/knLLAAa')
    if call.data == "deu6":
        bot.send_message(call.message.chat.id, 'https://de-oge.sdamgia.ru/')
    if call.data == "sp":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Аудирование', callback_data='sp1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Чтение', callback_data='sp2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Лекс-грамм',
                                           callback_data='sp3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Письмо',
                                           callback_data='sp4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Говорение',
                                           callback_data='sp5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='sp6')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "sp1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/DaQUFcw')
    if call.data == "sp2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/mrSRs2z')
    if call.data == "sp3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/pS28Sxd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/7QdnCG0')
    if call.data == "sp4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/0H7cLu4')
    if call.data == "sp5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/wn4iXdR')
    if call.data == "sp6":
        bot.send_message(call.message.chat.id, 'https://sp-oge.sdamgia.ru/')
    if call.data == "bio":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Биология как наука. Методы биологии', callback_data='bio1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Среда обитания. Природные и искусственные сообщества',
                                            callback_data='bio2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Эволюционное развитие растений, животных и человека',
                                           callback_data='bio3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Организмы бактерий, грибов и лишайников',
                                           callback_data='bio4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Растительный организм. Систематические группы растений',
                                           callback_data='bio5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Животный организм. Систематические группы животных',
                                           callback_data='bio6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Человек и его здоровье',
                                           callback_data='bio7')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='bio8')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "bio1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/SSMjeoJ')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/pZj0gWn')
    if call.data == "bio2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/RTwlzEd')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/Gonncba')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/O7TCA4R')
    if call.data == "bio3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/2VDRxZn')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/UHgWoWk')
    if call.data == "bio4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/UVPPeW1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/N27ZzI8')
    if call.data == "bio5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/oHn1d9v')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/UymO0j1')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/VHnw2UP')
    if call.data == "bio6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/mRyLX0K')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/q8ZCl6e')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/UtNGLTp')
    if call.data == "bio7":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/71bBzOD')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/lNrizW6')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/L2nDRRv')
    if call.data == "bio8":
        bot.send_message(call.message.chat.id, 'https://bio-oge.sdamgia.ru/')
    if call.data == "obch":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Человек и его социальное окружение', callback_data='obch1')
        keyboard.add(key_yes)

        ke_yes = types.InlineKeyboardButton(text='Общество, в котором мы живем',
                                            callback_data='obch2')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='Человек в мире культуры',
                                           callback_data='obch3')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Человек в экономических отношениях',
                                           callback_data='obch4')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Человек в системе социальных отношений',
                                           callback_data='obch5')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Человек в политическом измерении',
                                           callback_data='obch6')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Гражданин и государство',
                                           callback_data='obch7')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Человек как участник правовых отношений',
                                           callback_data='obch8')
        keyboard.add(key_o)
        key_o = types.InlineKeyboardButton(text='Практика',
                                           callback_data='obch9')
        keyboard.add(key_o)
        question = 'Выберите тему'
        bot.send_message(call.from_user.id, text=question, reply_markup=keyboard)
    if call.data == "obch1":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/fnn7zV7')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/eIoV2n3')
    if call.data == "obch2":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/n0Lre4i')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/raOGiXk')
    if call.data == "obch3":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/drk0IiV')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/ztOHAgs')
    if call.data == "obch4":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/6jMmP2K')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/63WZq3p')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/G9YlYh5')
    if call.data == "obch5":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/iQXSkNU')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/5a0tTtA')
    if call.data == "obch6":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/NjKg14E')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/kndElzb')
    if call.data == "obch7":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/cSXmTUx')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/zvipP8g')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/cqGIQeG')
    if call.data == "obch8":
        bot.send_photo(call.message.chat.id, 'https://imgur.com/5EVlxib')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/zrxwF85')
        bot.send_photo(call.message.chat.id, 'https://imgur.com/6poFI8H')
    if call.data == "obch9":
        bot.send_message(call.message.chat.id, 'https://soc-oge.sdamgia.ru/')
    if call.data == "dat1":
        bot.send_message(call.message.chat.id,
                         'Досрочный период\n'
                         '\n'
                         '(｡•́︿•̀｡) 22 апреля (вторник) — математика;\n'
                         '(╥﹏╥) 25 апреля (пятница) — русский язык;\n'
                         '(ಠ ∩ಠ) 29 апреля (вторник) — информатика, литература, обществознание, химия;\n'
                         '(｀Д´) 6 мая (вторник) — биология, география, иностранные языки (английский, испанский, '
                         'немецкий, французский), история, физика.\n'
                         '\n'
                         '\n'
                         'Резервные дни\n'
                         '\n'
                         '⋋_⋌12 мая (понедельник) — математика;\n'
                         '(╬ಠ益ಠ) 13 мая (вторник) — информатика, литература, обществознание, химия;\n'
                         '(ಥ﹏ಥ) 14 мая (среда) — биология, география, иностранные языки (английский, испанский, '
                         'немецкий, французский), история, физика;\n'
                         '(=ↀωↀ=) 15 мая (четверг) — русский язык;\n'
                         '༼ つ ◕_◕ ༽つ 17 мая (суббота) — по всем учебным предметам;\n')
    if call.data == "dat2":
        bot.send_message(call.message.chat.id,
                         'Основной период\n'
                         '\n'
                         '(｡•́︿•̀｡)  21 мая (среда) — иностранные языки (английский,\n'
                         ' испанский, немецкий, французский);\n'
                         '(╥﹏╥)  22 мая (четверг) — иностранные языки (английский, испанский, немецкий, французский);\n'
                         '(ಠ ∩ಠ)  26 мая (понедельник) — биология, информатика, обществознание, химия;\n'
                         '(｀Д´)  29 мая (четверг) — география, история, физика, химия;\n'
                         '⋋_⋌  3 июня (вторник) — математика;\n'
                         '(╬ಠ益ಠ)  6 июня (пятница) — география, информатика, обществознание;\n'
                         '(ಥ﹏ಥ)  9 июня (понедельник) — русский язык;\n'
                         '(=ↀωↀ=)  16 июня (понедельник) — биология, информатика, литература, физика.\n'
                         '\n'
                         '\n'
                         'Резервные дни\n'
                         '\n'
                         '(ꀄꀾꀄ) 26 июня(четверг) — русский язык;\n'
                         'ि०॰०ॢी 27 июня(пятница) — по всем учебным предметам(кроме русского языка и математики);\n'
                         '(ㅇㅅㅇ❀) 28 июня(суббота) — по всем учебным предметам(кроме русского языка и математики);\n'
                         'ฅ•ω•ฅ 30 июня(понедельник) — математика;\n'
                         '(๑˃ᴗ˂) ﻭ 1 июля(вторник) — по всем учебным предметам;\n'
                         'ㅇㅅㅇ 2 июля(среда) — по всем учебным предметам\n')
    if call.data == "dat3":
        bot.send_message(call.message.chat.id,
                         'Дополнительный период\n'
                         '\n'
                         '༼ꉺ౪ꉺ༽ 2 сентября (вторник) — математика;\n'
                         '༼ : ౦ ‸ ౦ : ༽ 5 сентября (пятница) — русский язык;\n'
                         '(ಥ﹏ಥ) 9 сентября (вторник) — биология, география, история, физика;\n'
                         '(ノ￣ー￣)ノ 12 сентября (пятница) — иностранные языки (английский, испанский, немецкий, '
                         'французский), информатика, литература, обществознание, химия.\n'
                         '\n'
                         '\n'
                         'Резервные дни\n'
                         '\n'
                         '༼⁰o⁰；༽ 17 сентября (среда) — русский язык;\n'
                         '(„ಡωಡ„) 18 сентября (четверг) — математика;\n'
                         '(´｡• ω •｡`)♡ 19 сентября (пятница) — по всем учебным предметам (кроме русского языка и '
                         'математики);\n'
                         '(♡-_-♡) 22 сентября (понедельник) — по всем учебным предметам (кроме русского языка и '
                         'математики);\n'
                         '(♡μ_μ) 23 сентября (вторник) — по всем учебным предметам.\n')


bot.polling(none_stop=True, interval=0)
