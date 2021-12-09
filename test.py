import unittest

from project import starosta
from project import globalkey
from project import date
from project import subject
from project import infot
from project import profile
from project import ploshad
from project import infos

class projecttest(unittest.TestCase):
    main_keyboard = [
        ['А с кем я учусь?🤔'],
        ['Мои преподаватели👨'],
        ['Мои Дисциплины📖'],
        ['Может начать готовиться к сессии?😴'],
    ]
    
    keyboard1 = [
        ['Cписок преподавателей🧾'],
        ['Площадка проведения занятий💻'],
        ['Профили на сайте ВШЭ📱'],
    ]
    
    def test_infos(self):
        self.assertEqual(profile(''), 'error')
    
    def test_ploshad(self):
        self.assertNotEqual(profile('площадка'),'\n\nМат. Анализ, Физика Лекция, Информатика - MS Teams\n\nФизика Семинар - Google Meet\n\nАиП Лекции - Even Webinar\n\nАиП Семинар - Meet Miem')
    
    def test_profile(self):
        self.assertEqual(profile(''),'error')
    
    def test_starosta(self):
        self.assertNotEqual(starosta('зам'),'\nЯрославский Андрей - староста группы БИБ211\nПочта: avyaroslavskiy@edu.hse.ru\n\nФатхутдинов Никита - зам. старосты\nПочта: nifatkhutdinov@edu.hse.ru\n\nТамара Цкиманаури и Альберт Назаретян - кураторы группы БИБ211')

    def test_keyboard1(self):
        self.assertNotEqual(infot(),self.keyboard1)
        
    def test_keyboard(self):
        self.assertNotEqual(globalkey(),self.main_keyboard)
        
    def test_date(self):
        self.assertEqual(date('Пицца'), 'error')
    
    def test_subject1(self):
        self.assertNotEqual(subject('Предмет'), '\nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория')
        

if __name__ == "__main__":
    unittest.main()
