import unittest
from datetime import datetime

from core.domain.person import Person


class TestPerson(unittest.TestCase):
    def test_age_calculation(self):
        person = Person(first_name="John", last_name="Doe", birth_date=datetime(1990, 5, 20))
        expected_age = datetime.today().year - 1990 - (datetime.today().month < 5 or
                                                       (datetime.today().month == 5 and datetime.today().day < 20))
        self.assertEqual(person.age, expected_age)

    def test_age_calculation_birthday_today(self):
        today = datetime.today()
        person = Person(first_name="Jane", last_name="Smith",
                        birth_date=datetime(today.year - 30, today.month, today.day))
        self.assertEqual(person.age, 30)

    def test_age_calculation_upcoming_birthday(self):
        person = Person(first_name="Alice", last_name="Johnson", birth_date=datetime(1995, 12, 31))
        expected_age = datetime.today().year - 1995 - (datetime.today().month < 12 or
                                                       (datetime.today().month == 12 and datetime.today().day < 31))
        self.assertEqual(person.age, expected_age)

    def test_age_leap_year(self):
        person = Person(first_name="Leo", last_name="Martin", birth_date=datetime(2000, 2, 29))
        today = datetime.today()
        expected_age = today.year - 2000 - (
                (today.month, today.day) < (
        2, 28 if not (today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)) else 29)
        )
        self.assertEqual(person.age, expected_age)


if __name__ == '__main__':
    unittest.main()
