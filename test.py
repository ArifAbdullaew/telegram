import telebot
from forex_python.converter import CurrencyRates
import requests as r

bot = telebot.TeleBot('5097652539:AAFzQpvariYOIC8u70rSCzB1uRZ3CkpllYk', parse_mode='html')

COMMANDS = ['start', 'infos', 'infot', 'subject', 'date', 'starosta']


@bot.message_handler(commands=COMMANDS)
def start_message(message) -> None:
    '''
        Главная функция, обрабатывающая команды, полученные от пользователя
    '''

    keyboard = get_main_keyboard()

    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}</b>,  \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/infos - информация о студентах!\n/infot - информация о преподавателях\n/date - даты ближайших работ!\n/subject - набор дисциплин 21/22!\n/starosta - Кто является старостой и куратором БИБ211', reply_markup=keyboard)

    elif message.text.lower() == '/infos':
        infos(message)

    elif message.text.lower() == '/subject':
        subject(message)

    elif message.text.lower() == '/infot':
        infot(message)

    elif message.text.lower() == '/date':
        date(message)
        
    elif message.text.lower() == '/starosta':
        starosta(message)


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
        bot.send_message(message.chat.id, 'И снова здравствуй, и снова привет  \n\n/infos - информация о студентах!\n/infot - информация о преподавателях\n/date - даты ближайших работ!\n/subject - набор дисциплин 21/22!\n/starosta - представительские лица', reply_markup=keyboard)

    elif 'предмет' in message.text.lower() or 'пред' in message.text.lower() or 'дисциплины' in message.text.lower():
        subject(message)

    elif 'зам' in message.text.lower() or 'стар' in message.text.lower() or 'староста' in message.text.lower() or 'куратор' in message.text.lower() or 'кураторы' in message.text.lower() or 'курат' in message.text.lower():
        starosta(message)
        
    else:
        bot.send_message(
            message.chat.id, "\nНу тут мои полномочия все \n тут уж извините, но все ")


def get_main_keyboard() -> telebot.types.ReplyKeyboardMarkup:
    '''
        Функция, возвращающая главные кнопки нашего бота
    '''

    main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_keyboard.row('А с кем я учусь?🤔', 'Мои преподаватели👨‍🏫')
    main_keyboard.row('Мои Дисциплины📖', 'Может начать готовиться к сессии?😴')

    return main_keyboard


def date(message) -> None:
    try:
        bot.send_message(message.chat.id, f'\n\nАлгоритмизация и программирование - 20.12.21\n\nИстория - 21.12.21\n\nИнформатика - 22.12.21\n\nМатематический анализ - 23.12.21')
    except:
        bot.send_message(message.chat.id, 'Я конечно люблю программировать, но не настолько, чтобы решать данную проблему👨‍💻', reply_markup=get_main_keyboard())



def infos(message) -> None:
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Возвращаемся обратно 🚀 ')
    bot.send_message(message.chat.id, f'\nАбдуллаев Ариф\n\nАбзах Баян Амер Мохд Амин\n\nАбраменко Александр\n\nАрхипочкин Александр\n\nБaлясникова Екатерина\n\nБелоус Александр\n\nВоронов Арсений\n\nГурбатова Елизавета\n\nГусев Максим\n\nДронова Алла\n\nЕлецкая Елизавета\n\nКайнова Мария\n\nКлепацкий Даниил\n\nКинякин Владислав\n\nКогут Михаил\n', reply_markup=keyboard)
    bot.send_message(message.chat.id, f'\nКолдышев Пётр\n\nКрохин Алексей\n\nКрутоног Максим\n\nМиллер Ян\n\nПегай Владислав\n\nПлешков Иван\n\nСавин Даниил\n\nСемененя Александра\n\nТаньчев Алексей\n\nТимошкин Павел\n\nТуманов Александр\n\nФатхутдинов Никита зам. старосты \n\nХрупов Андрей\n\nЯрославский Александр староста \n\nМамута Александр\n', reply_markup=keyboard)
        

def starosta(message) -> None:
        try:
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row('Возвращаемся обратно 🚀 ')
            bot.send_message(message.chat.id, f'\nЯрославский Андрей - староста группы БИБ211\nПочта: avyaroslavskiy@edu.hse.ru\n\nФатхутдинов Никита - зам. старосты\nПочта: nifatkhutdinov@edu.hse.ru\n\nТамара Цкиманаури и Альберт Назаретян - кураторы группы БИБ211', reply_markup=keyboard)
        except:
            bot.send_message(message.chat.id, 'Братишка, ты что-то не то делаешь👮🏼‍♂️', reply_markup=get_main_keyboard())
      
      


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

def subject(message) -> None:
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, f'\nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория', reply_markup=keyboard)
    


bot.polling()
