import telebot
from telebot import types

bot = telebot.TeleBot(
    '5097652539:AAFzQpvariYOIC8u70rSCzB1uRZ3CkpllYk', parse_mode='html')

COMMANDS = ['start', 'infos', 'infot', 'subject',
            'date', 'starosta', 'spisok', 'ploshad', 'profile']


@bot.message_handler(commands=COMMANDS)
def start_message(message) -> None:
    '''
        Главная функция, обрабатывающая команды, полученные от пользователя
    '''

    keyboard = globalkey()

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
    if 'одногруппники' in message.text.lower() or 'студенты' in message.text.lower() or 'с кем' in message.text.lower() or 'одногруппник' in message.text.lower():
        infos(message)

    elif 'Препод' in message.text.lower() or 'преподаватели' in message.text.lower() or 'Преп' in message.text.lower():
        infot(message)

    elif 'сессия' in message.text.lower() or 'экзамен' in message.text.lower() or 'отчисление' in message.text.lower() or 'сессии' in message.text.lower():
        date(message)

    elif 'начало' in message.text.lower() or 'обратно' in message.text.lower():
        keyboard = globalkey()
        bot.send_message(message.chat.id, 'И снова здравствуй, и снова привет  \n\n/infos - информация о студентах!\n/infot - информация о преподавателях\n/date - даты ближайших работ!\n/subject - набор дисциплин 21/22!\n/starosta - представительские лица', reply_markup=keyboard)

    elif 'предмет' in message.text.lower() or 'пред' in message.text.lower() or 'дисциплины' in message.text.lower():
        subject(message)

    elif 'зам' in message.text.lower() or 'стар' in message.text.lower() or 'староста' in message.text.lower() or 'куратор' in message.text.lower() or 'кураторы' in message.text.lower() or 'курат' in message.text.lower():
        starosta(message)

    elif 'Список' in message.text.lower() or 'преподавателей' in message.text.lower():
        spisok(message)

    elif 'площадка' in message.text.lower():
        ploshad(message)

    elif 'вшэ' in message.text.lower():
        profile(message)

    else:
        bot.send_message(
            message.chat.id, "\nНу тут мои полномочия все \n тут уж извините, но все ")


def globalkey() -> telebot.types.ReplyKeyboardMarkup:
    '''
        Функция, возвращающая главные кнопки нашего бота
    '''
    try:
        main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        main_keyboard.row('А с кем я учусь?🤔', 'Мои преподаватели👨')
        main_keyboard.row('Мои Дисциплины📖', 'Может начать готовиться к сессии?😴')

        return main_keyboard
    except:
        return 'error'


def date(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(
            message.chat.id, f'\n\nАлгоритмизация и программирование - 20.12.21\n\nИстория - 21.12.21\n\nИнформатика - 22.12.21\n\nМатематический анализ - 23.12.21', reply_markup=keyboard)
    except:
        return 'error'


def infos(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\nАбдуллаев Ариф\n\nАбзах Баян Амер Мохд Амин\n\nАбраменко Александр\n\nАрхипочкин Александр\n\nБaлясникова Екатерина\n\nБелоус Александр\n\nВоронов Арсений\n\nГурбатова Елизавета\n\nГусев Максим\n\nДронова Алла\n\nЕлецкая Елизавета\n\nКайнова Мария\n\nКлепацкий Даниил\n\nКинякин Владислав\n\nКогут Михаил\n', reply_markup=keyboard)
        bot.send_message(message.chat.id, f'\nКолдышев Пётр\n\nКрохин Алексей\n\nКрутоног Максим\n\nМиллер Ян\n\nПегай Владислав\n\nПлешков Иван\n\nСавин Даниил\n\nСемененя Александра\n\nТаньчев Алексей\n\nТимошкин Павел\n\nТуманов Александр\n\nФатхутдинов Никита зам. старосты \n\nХрупов Андрей\n\nЯрославский Александр староста \n\nМамута Александр\n', reply_markup=keyboard)
    except:
        return 'error'


def starosta(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\nЯрославский Андрей - староста группы БИБ211\nПочта: avyaroslavskiy@edu.hse.ru\n\nФатхутдинов Никита - зам. старосты\nПочта: nifatkhutdinov@edu.hse.ru\n\nТамара Цкиманаури и Альберт Назаретян - кураторы группы БИБ211', reply_markup=keyboard)
    except:
        return 'error'


def infot(message) -> None:
    '''
        Функция, на которой мы страшиваем у пользователя, что конерктно надо .
    '''
    try:
        keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.row('Cписок преподавателей🧾', 'Площадка проведения занятий💻')
        keyboard1.row('Профили на сайте ВШЭ📱')
        bot.send_message(
            message.chat.id, f'<b>{message.from_user.first_name}</b>, что вы желаете?', reply_markup=keyboard1)
    except: 
        return 'error'


def spisok(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\nАртамонов Сергей Юрьевич - Мат. Анализ\n \nГеращенко Людмила Андреевна - Информатика\n \nКрещук Алексей Андреевич - АиП лекции\n \nДерендяев Александр Борисович - АиП семинар\n \nШаненко Аркадий Аркадьевич - Физика Лекции\n \nВолкова Ирина Владимировна - История\n \nГузенкова Александра Сергеевна - Физика Семинар\n \nАльбатша Ахмад Мухаммад Хусайн - Информатика Практическое занятие', reply_markup=keyboard)
    except:
        return 'error'


def ploshad(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\n\nМат. Анализ, Физика Лекция, Информатика - MS Teams\n\nФизика Семинар - Google Meet\n\nАиП Лекции - Even Webinar\n\nАиП Семинар - Meet Miem', reply_markup=keyboard)
    except:
        return 'error'


def profile(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(
            message.chat.id, f'https://www.hse.ru/ba/is/tutors', reply_markup=keyboard)
    except:
        return 'error'


def subject(message) -> None:
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, f'\nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория', reply_markup=keyboard)
    except:
        return 'error'

bot.polling()
