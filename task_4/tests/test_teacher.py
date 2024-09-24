import unittest
from datetime import datetime

from core.domain import Student, Teacher


class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher(
            first_name="Sarah",
            last_name="Connor",
            birth_date=datetime(1980, 3, 25),
            subjects=["Химия", "Физика"]
        )

    def test_initialization(self):
        self.assertEqual(self.teacher.first_name, "Sarah")
        self.assertEqual(self.teacher.last_name, "Connor")
        self.assertEqual(self.teacher.subjects, ["Химия", "Физика"])
        self.assertEqual(self.teacher.students, [])

    def test_is_valid_teacher_valid(self):
        self.assertTrue(self.teacher.is_valid_teacher)

    def test_is_valid_teacher_invalid(self):
        young_teacher = Teacher(
            first_name="Anna",
            last_name="Smith",
            birth_date=datetime(2005, 7, 20),
            subjects=["Физика"]
        )
        self.assertFalse(young_teacher.is_valid_teacher)

        old_teacher = Teacher(
            first_name="John",
            last_name="Doe",
            birth_date=datetime(1950, 1, 1),
            subjects=["Химия"]
        )
        self.assertFalse(old_teacher.is_valid_teacher)

    def test_assign_student(self):
        student = Student(
            first_name="Alex",
            last_name="Jones",
            birth_date=datetime(2008, 6, 12),
            grade=10
        )
        self.teacher.assign_student(student)
        self.assertIn(student, self.teacher.students)

    def test_assign_student_no_duplicates(self):
        student = Student(
            first_name="Alex",
            last_name="Jones",
            birth_date=datetime(2008, 6, 12),
            grade=10
        )
        self.teacher.assign_student(student)
        self.teacher.assign_student(student)
        self.assertEqual(len(self.teacher.students), 1)

    def test_str_method(self):
        expected_str = "Учитель Sarah Connor, Предметы: Химия, Физика, Возраст: 44"
        self.assertEqual(str(self.teacher), expected_str)


if __name__ == '__main__':
    unittest.main()
