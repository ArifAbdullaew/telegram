import unittest

from project import text_processing
from project import globalkey
from project import date
from project import subject
from project import infot


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
    
    def test_keyboard1(self):
        self.assertNotEqual(infot(),self.keyboard1)

    def test_keyboard(self):
        self.assertEqual(globalkey(),self.main_keyboard)
        
    def test_keyboard(self):
        self.assertNotEqual(globalkey(),self.main_keyboard)
        
    def test_date(self):
        self.assertEqual(date('Пицца'), 'error')
    
    def test_subject1(self):
        self.assertNotEqual(subject('Предмет'), '\nМатематический Анализ\n\nИнформатика\n\nАлгоритмизация и Программирование\n\nПроектный семинар по Информационной безопасности\n\nКомпьютерный практикум Администрирование систем и сетей\n\nФизика\n\nИстория')
        
    def text_processing(self):
        self.assertEqual(text_processing('triplex'),'\nНу тут мои полномочия все \n тут уж извините, но все ')
      

if __name__ == "__main__":
    unittest.main()
