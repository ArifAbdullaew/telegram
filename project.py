# -*- coding: utf-8 -*-
import telebot
from telebot import types
from kluchik import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode='html')



@bot.message_handler(commands=['start'])
def start_message(message) -> None:
    '''
        Главная функция, обрабатывающая команды, полученные от пользователя
    '''
    keyboard = globalkey()
    bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}</b>,  \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/infos - информация о студентах!\n\n/infot - информация о преподавателях\n\n/date - даты ближайших работ!\n\n/subject - набор дисциплин 21/22!\n\n/starosta - Кто является старостой и куратором БИБ211', reply_markup=keyboard)

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
    
@bot.message_handler(commands=['infos'])
@bot.message_handler(content_types=['text'], regexp = 'одногруппники?|студенты|с кем')
def infos(message) -> None:    
    '''
        Функция, на которую выдаем список группы .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\nАбдуллаев Ариф\n\nАбзах Баян Амер Мохд Амин\n\nАбраменко Александр\n\nАрхипочкин Александр\n\nБaлясникова Екатерина\n\nБелоус Александр\n\nВоронов Арсений\n\nГурбатова Елизавета\n\nГусев Максим\n\nДронова Алла\n\nЕлецкая Елизавета\n\nКайнова Мария\n\nКлепацкий Даниил\n\nКинякин Владислав\n\nКогут Михаил\n\nКолдышев Пётр\n\nКрохин Алексей\n\nКрутоног Максим\n\nМиллер Ян\n\nПегай Владислав\n\nПлешков Иван\n\nСавин Даниил\n\nСемененя Александра\n\nТаньчев Алексей\n\nТимошкин Павел\n\nТуманов Александр\n\nФатхутдинов Никита зам. старосты \n\nХрупов Андрей\n\nЯрославский Александр староста \n\nМамута Александр\n', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['date'])   
@bot.message_handler(content_types=['text'], regexp = 'сессии')
def date(message) -> None:
    '''
        Функция, на которую выдаем дисциплины .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(
            message.chat.id, f'\n\nАлгоритмизация и программирование - 20.12.21\n\nИстория - 21.12.21\n\nИнформатика - 22.12.21\n\nМатематический анализ - 23.12.21', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['again'])
@bot.message_handler(content_types=['text'], regexp = 'обратно|начало')
def again(message) -> None:
    '''
        Функция, возврата .
    '''
    try:
        keyboard = globalkey()
        bot.send_message(message.chat.id, 'И снова здравствуй, и снова привет  \n\n/infos - информация о студентах!\n\n/infot - информация о преподавателях\n\n/date - даты ближайших работ!\n\n/subject - набор дисциплин 21/22!\n\n/starosta - представительские лица', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['subject'])
@bot.message_handler(content_types=['text'], regexp = 'предмет|пред|дисциплины')
def subject(message) -> None:
    '''
        Функция, на которую выдает список дисциплин .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, f'\nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['infot'])
@bot.message_handler(content_types=['text'], regexp = 'преподаватели')
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

@bot.message_handler(commands=['starosta'])   
@bot.message_handler(content_types=['text'], regexp = 'зам|стар|староста|куратор|кураторы|курат')
def starosta(message) -> None:
    '''
        Функция, на которую выдаем старосты .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\nЯрославский Андрей - староста группы БИБ211\nПочта: avyaroslavskiy@edu.hse.ru\n\nФатхутдинов Никита - зам. старосты\nПочта: nifatkhutdinov@edu.hse.ru\n\nТамара Цкиманаури и Альберт Назаретян - кураторы группы БИБ211', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['spisok'])
@bot.message_handler(content_types=['text'],regexp = 'список|Cписок преподавателей🧾|Список')
def spisok(message) -> None:
    '''
        Функция, на которую выдает список учителей .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\nАртамонов Сергей Юрьевич - Мат. Анализ\n \nГеращенко Людмила Андреевна - Информатика\n \nКрещук Алексей Андреевич - АиП лекции\n \nДерендяев Александр Борисович - АиП семинар\n \nШаненко Аркадий Аркадьевич - Физика Лекции\n \nВолкова Ирина Владимировна - История\n \nГузенкова Александра Сергеевна - Физика Семинар\n \nАльбатша Ахмад Мухаммад Хусайн - Информатика Практическое занятие', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['ploshad'])
@bot.message_handler(content_types=['text'], regexp = 'площадка')
def ploshad(message) -> None:
    '''
        Функция, на которую выдает список платформ .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(message.chat.id, f'\n\nМат. Анализ, Физика Лекция, Информатика - MS Teams\n\nФизика Семинар - Google Meet\n\nАиП Лекции - Even Webinar\n\nАиП Семинар - Meet Miem', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler(commands=['profile'])
@bot.message_handler(content_types=['text'], regexp = 'вшэ|профиль|проф')
def profile(message) -> None:
    '''
        Функция, на которую выдает сайт с  преподваталеями .
    '''
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Возвращаемся обратно 🚀 ')
        bot.send_message(
            message.chat.id, f'https://www.hse.ru/ba/is/tutors', reply_markup=keyboard)
    except:
        return 'error'

@bot.message_handler()
def error(message):
    bot.send_message(
                message.chat.id, "\nНу тут мои полномочия все \n тут уж извините, но все ")

bot.polling()
