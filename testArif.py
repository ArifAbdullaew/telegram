# -*- coding: utf-8 -*-
import unittest
from mock.mock import MagicMock
import unittest
import mock
import projectArif
from unittest.mock import MagicMock


class telegrambot_test(unittest.TestCase):

    @mock.patch('projectArif.bot')
    def test_start(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.start_message(message)
        ret = f'<b>{name}</b>,  \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/infos - информация о студентах!\n\n/infot - информация о преподавателях\n\n/date - даты ближайших работ!\n\n/subject - набор дисциплин 21/22!\n\n/starosta - Кто является старостой и куратором БИБ211'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 

    @mock.patch('projectArif.bot')
    def test_date(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.date(message)
        ret = f'<b>{name}</b>, \n\nАлгоритмизация и программирование - 20.12.21\n\nИстория - 21.12.21\n\nИнформатика - 22.12.21\n\nМатематический анализ - 23.12.21'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 
        
    @mock.patch('projectArif.bot')
    def test_infot(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.infot(message)
        ret = f'<b>{name}</b>, \nАбдуллаев Ариф\n\nАбзах Баян Амер Мохд Амин\n\nАбраменко Александр\n\nАрхипочкин Александр\n\nБaлясникова Екатерина\n\nБелоус Александр\n\nВоронов Арсений\n\nГурбатова Елизавета\n\nГусев Максим\n\nДронова Алла\n\nЕлецкая Елизавета\n\nКайнова Мария\n\nКлепацкий Даниил\n\nКинякин Владислав\n\nКогут Михаил\n\nКолдышев Пётр\n\nКрохин Алексей\n\nКрутоног Максим\n\nМиллер Ян\n\nПегай Владислав\n\nПлешков Иван\n\nСавин Даниил\n\nСемененя Александра\n\nТаньчев Алексей\n\nТимошкин Павел\n\nТуманов Александр\n\nФатхутдинов Никита зам. старосты \n\nХрупов Андрей\n\nЯрославский Александр староста \n\nМамута Александр\n'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 
        

    @mock.patch('projectArif.bot')
    def test_again(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.again(message)
        ret = f'<b>{name}</b>, И снова здравствуй, и снова привет  \n\n/infos - информация о студентах!\n\n/infot - информация о преподавателях\n\n/date - даты ближайших работ!\n\n/subject - набор дисциплин 21/22!\n\n/starosta - представительские лица'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 

    @mock.patch('projectArif.bot')
    def test_subject(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.subject(message)
        ret = f'<b>{name}</b>, \nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 
        
    @mock.patch('projectArif.bot')
    def test_starosta(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.starosta(message)
        ret = f'<b>{name}</b>, \nЯрославский Андрей - староста группы БИБ211\nПочта: avyaroslavskiy@edu.hse.ru\n\nФатхутдинов Никита - зам. старосты\nПочта: nifatkhutdinov@edu.hse.ru\n\nТамара Цкиманаури и Альберт Назаретян - кураторы группы БИБ211'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 

    @mock.patch('projectArif.bot')
    def test_spisok(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.spisok(message)
        ret = f'<b>{name}</b>, \nАртамонов Сергей Юрьевич - Мат. Анализ\n \nГеращенко Людмила Андреевна - Информатика\n \nКрещук Алексей Андреевич - АиП лекции\n \nДерендяев Александр Борисович - АиП семинар\n \nШаненко Аркадий Аркадьевич - Физика Лекции\n \nВолкова Ирина Владимировна - История\n \nГузенкова Александра Сергеевна - Физика Семинар\n \nАльбатша Ахмад Мухаммад Хусайн - Информатика Практическое занятие'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 

    @mock.patch('projectArif.bot')
    def test_ploshad(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.ploshad(message)
        ret = f'<b>{name}</b>, \n\nМат. Анализ, Физика Лекция, Информатика - MS Teams\n\nФизика Семинар - Google Meet\n\nАиП Лекции - Even Webinar\n\nАиП Семинар - Meet Miem'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 

    @mock.patch('projectArif.bot')
    def test_profile(self, bot):
        name = 'test'
        user = MagicMock(first_name=name)
        chat = MagicMock(id=123)
        message = MagicMock(from_user=user,chat=chat)
        projectArif.profile(message)
        ret = f'<b>{name}</b>, https://www.hse.ru/ba/is/tutors'
        bot.send_message.assert_called_with(123, ret, reply_markup=any) 

if __name__ == "__main__":
    unittest.main()
