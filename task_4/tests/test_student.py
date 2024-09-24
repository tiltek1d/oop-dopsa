import unittest
from datetime import datetime

from core.domain import Student, Teacher


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(first_name="Alex", last_name="Smith", birth_date=datetime(2008, 5, 15), grade=10)

    def test_initialization(self):
        self.assertEqual(self.student.first_name, "Alex")
        self.assertEqual(self.student.last_name, "Smith")
        self.assertEqual(self.student.grade, 10)
        self.assertEqual(self.student.teachers, [])

    def test_is_valid_student_under_18(self):
        self.assertTrue(self.student.is_valid_student)

    def test_is_valid_student_over_18(self):
        adult_student = Student(first_name="John", last_name="Doe", birth_date=datetime(2000, 5, 15), grade=12)
        self.assertFalse(adult_student.is_valid_student)

    def test_assign_teacher(self):
        teacher = Teacher(
            first_name="Mr.",
            last_name="Anderson",
            birth_date=datetime.strptime('12-12-1990', '%d-%m-%Y'),
            subjects=['Химия'],
        )
        self.student.assign_teacher(teacher)
        self.assertIn(teacher, self.student.teachers)

    def test_str_method(self):
        expected_str = f"Ученик Alex Smith, Класс: 10, Возраст: {self.student.age}"
        self.assertEqual(str(self.student), expected_str)


if __name__ == '__main__':
    unittest.main()
