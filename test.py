import unittest

from project import date
from project import globalkey

class test(unittest.TestCase):
    Keyboard = [
        ['А с кем я учусь?🤔'],
        ['Мои преподаватели👨‍🏫'],
        ['Мои Дисциплины📖'],
        ['Может начать готовиться к сессии?😴'],
    ]

    def test_klava(self):
        self.assertNotEqual(globalkey(), self.Keyboard)
        
    def test_date(self):
        self.assertEqual(date('Информатика'))


if __name__ == "__main__":
    unittest.main()