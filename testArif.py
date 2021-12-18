# -*- coding: utf-8 -*-
import unittest
from telethon import TelegramClient
import unittest
import time


# Вот сюда Апи и Хэщ
api_id = int('10445218')
api_hash = "6fa8da898c1f3285adaa28c8ff5d883d"
client = TelegramClient('Airf', api_id, api_hash)


client.start()


class telegrambot_test(unittest.TestCase):
    def test_start(self):
        try:
            client.send_message('@hsemiembib211_bot', 'start')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Airf,  \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/infos - информация о студентах!\n\n/infot - информация о преподавателях\n\n/date - даты ближайших работ!\n\n/subject - набор дисциплин 21/22!\n\n/starosta - Кто является старостой и куратором БИБ211'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_infos(self):
        try:
            client.send_message('@hsemiembib211_bot', 'А с кем я учусь?🤔')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'\nАбдуллаев Ариф\n\nАбзах Баян Амер Мохд Амин\n\nАбраменко Александр\n\nАрхипочкин Александр\n\nБaлясникова Екатерина\n\nБелоус Александр\n\nВоронов Арсений\n\nГурбатова Елизавета\n\nГусев Максим\n\nДронова Алла\n\nЕлецкая Елизавета\n\nКайнова Мария\n\nКлепацкий Даниил\n\nКинякин Владислав\n\nКогут Михаил\n\nКолдышев Пётр\n\nКрохин Алексей\n\nКрутоног Максим\n\nМиллер Ян\n\nПегай Владислав\n\nПлешков Иван\n\nСавин Даниил\n\nСемененя Александра\n\nТаньчев Алексей\n\nТимошкин Павел\n\nТуманов Александр\n\nФатхутдинов Никита зам. старосты \n\nХрупов Андрей\n\nЯрославский Александр староста \n\nМамута Александр\n'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_subject(self):
        try:
            client.send_message('@hsemiembib211_bot', 'Мои Дисциплины📖')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'\nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_date(self):
        try:
            client.send_message('@hsemiembib211_bot',
                                'Может начать готовиться к сессии?😴')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'\n\nАлгоритмизация и программирование - 20.12.21\n\nИстория - 21.12.21\n\nИнформатика - 22.12.21\n\nМатематический анализ - 25.12.21'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_spisok(self):
        try:
            client.send_message('@hsemiembib211_bot', 'Cписок преподавателей🧾')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'\nАртамонов Сергей Юрьевич - Мат. Анализ\n \nГеращенко Людмила Андреевна - Информатика\n \nКрещук Алексей Андреевич - АиП лекции\n \nДерендяев Александр Борисович - АиП семинар\n \nШаненко Аркадий Аркадьевич - Физика Лекции\n \nВолкова Ирина Владимировна - История\n \nГузенкова Александра Сергеевна - Физика Семинар\n \nАльбатша Ахмад Мухаммад Хусайн - Информатика Практическое занятие'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_ploshad(self):
        try:
            client.send_message('@hsemiembib211_bot',
                                'Площадка проведения занятий💻')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'\n\nМат. Анализ, Физика Лекция, Информатика - MS Teams\n\nФизика Семинар - Google Meet\n\nАиП Лекции - Even Webinar\n\nАиП Семинар - Meet Miem'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_profile(self):
        try:
            client.send_message('@hsemiembib211_bot', 'Профили на сайте ВШЭ📱')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'https://www.hse.ru/ba/is/tutors'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_again(self):
        try:
            client.send_message('@hsemiembib211_bot',
                                'Возвращаемся обратно 🚀 ')
            time.sleep(2)
            messages = client.get_messages('@hsemiembib211_bot')
            for message in client.get_messages('@hsemiembib211_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'И снова здравствуй, и снова привет  \n\n/infos - информация о студентах!\n\n/infot - информация о преподавателях\n\n/date - даты ближайших работ!\n\n/subject - набор дисциплин 21/22!\n\n/starosta - представительские лица'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
            
           
        
        
