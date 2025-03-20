import telebot
from telebot import types

bot = telebot.TeleBot('а вот это вот только у меня, извините')

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да, это моя мечта', callback_data='q')
        keyboard.add(key_yes)
        ke_yes = types.InlineKeyboardButton(text='Мне бы хотелось', callback_data='w')
        keyboard.add(ke_yes)
        key_o = types.InlineKeyboardButton(text='У меня отсутствует уверенность..',
                                           callback_data='e')
        keyboard.add(key_o)
        key_ys = types.InlineKeyboardButton(text='Ненене! Мне еще проект по лицею и делать и огэ писать!',
                                            callback_data='r')
        keyboard.add(key_ys)
        question = 'Хочешь распилим тебя болгаркой? :)'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "q":
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "w":
        bot.send_message(call.message.chat.id, 'ЙЦЙ : )')
    elif call.data == "e":
        bot.send_message(call.message.chat.id, 'ЙЦЙ : )')
    else:
        bot.send_message(call.message.chat.id, 'ЙЦЙ : )')


bot.polling(none_stop=True, interval=0)
