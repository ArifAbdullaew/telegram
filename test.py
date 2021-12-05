import telebot
from forex_python.converter import CurrencyRates
import requests as r

bot = telebot.TeleBot(
    '5097652539:AAFzQpvariYOIC8u70rSCzB1uRZ3CkpllYk', parse_mode='html')

COMMANDS = ['start', 'infos', 'infot', 'subject', 'date']


@bot.message_handler(commands=COMMANDS)
def start_message(message) -> None:
    '''
        Главная функция, обрабатывающая команды, полученные от пользователя
    '''

    keyboard = get_main_keyboard()

    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'<b>{message.from_user.username}</b>,  \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/infos - информация о студентах!\n/infot - информация о преподавателях\n/date - даты ближайших работ!\n/subject - набор дисциплин 21/22!', reply_markup=keyboard)

    elif message.text.lower() == '/infos':
        infos(message)

    elif message.text.lower() == '/subject':
        sub(message)

    elif message.text.lower() == '/infot':
        infot(message)

    elif message.text.lower() == '/date':
        date(message)


@bot.message_handler(content_types=['text'])
def text_processing(message) -> None:
    '''
        Функция обработки обыного текста от пользователя
    '''

    if 'одногруппники' in message.text.lower() or 'студенты' in message.text.lower() or 'братья' in message.text.lower() or 'сестра' in message.text.lower() or 'одногруппник' in message.text.lower():
        infos(message)

    elif 'Препод' in message.text.lower() or 'Преподаватели' in message.text.lower() or 'Преп' in message.text.lower():
        infot(message)

    elif 'сессия' in message.text.lower() or 'экзамен' in message.text.lower() or 'отчисление' in message.text.lower():
        date(message)

    elif 'начало' in message.text.lower():
        keyboard = get_main_keyboard()
        bot.send_message(message.chat.id, 'И снова здравствуй, и снова привет  \n\n/infos - информация о студентах!\n/infot - информация о преподавателях\n/date - даты ближайших работ!\n/subject - набор дисциплин 21/22!', reply_markup=keyboard)

    elif 'предмет' in message.text.lower() or 'пред' in message.text.lower() or 'дисциплины' in message.text.lower():
        sub(message)

    else:
        bot.send_message(
            message.chat.id, " Ну тут мои полномочия все \n тут уж извините, но все ")


def get_main_keyboard() -> telebot.types.ReplyKeyboardMarkup:
    '''
        Функция, возвращающая главные кнопки нашего бота
    '''

    main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_keyboard.row('А с кем я учусь?🤔', 'Мои преподаватели👨‍🏫')
    main_keyboard.row('Мои Дисциплины📖', 'Может начать готовиться к сессии?😴')

    return main_keyboard


def date(message) -> None:

    return ''


def check_math_answer(message, answer) -> None:
    return ''


def infos(message):

    return  


def infot(message) -> None:
    '''
        Функция, на которой мы страшиваем у пользователя валютную пару.
    '''

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Cписок преподаватлей ', 'Площадка проведения занятий', )
    keyboard.row('Профиль на Сайте ВШЭ')

    bot.send_message(
        message.chat.id, f'<b>{message.from_user.first_name}</b>, выберите интересующую вас информацию 🤩', reply_markup=keyboard)
    bot.register_next_step_handler(message, teacherinf)


def teacherinf(message) -> None:
    return ''


def sub(message, pair) -> None:
    return ''


bot.polling()
