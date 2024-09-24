import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

from core.domain import Student, Teacher, SchoolSystem
from core.exceptions import StudentsAgeException, TeachersAgeException, NoSuitableTeacherException


class TestSchoolSystem(unittest.TestCase):
    def setUp(self):
        self.school_system = SchoolSystem(verbose=False)
        self.student = Student(first_name="Alex", last_name="Smith", birth_date=datetime(2008, 5, 15), grade=5)
        self.teachers = [
            Teacher(
                "Светлана", "Смирнова",
                datetime.strptime("15-06-1980", '%d-%m-%Y'),
                ["Математика", "Русский язык"]
            ),
            Teacher(
                "Ольга", "Кузнецова",
                datetime.strptime("10-02-1975", '%d-%m-%Y'),
                ["Физика", "Информатика", "Науки о природе"]
            ),
            Teacher(
                "Иван", "Попов",
                datetime.strptime("20-09-1990", '%d-%m-%Y'),
                ["Химия", "Биология", "Науки о природе"]
            ),
            Teacher(
                "Александр", "Соколов",
                datetime.strptime("25-03-1985", '%d-%m-%Y'),
                ["Русский язык", "Биология"]
            ),
            Teacher(
                "Мария", "Лебедева",
                datetime.strptime("30-07-1978", '%d-%m-%Y'),
                ["Физика", "Информатика"]
            ),
        ]

    def add_teachers(self):
        for teacher in self.teachers:
            self.school_system.add_teacher(teacher)

    def test_add_valid_student(self):
        self.add_teachers()
        self.school_system.add_student(self.student)
        self.assertIn(self.student, self.school_system.students)

    def test_add_invalid_student(self):
        invalid_student = Student(first_name="John", last_name="Doe", birth_date=datetime(2000, 5, 15), grade=12)
        with self.assertRaises(StudentsAgeException):
            self.school_system.add_student(invalid_student)

    def test_add_valid_teacher(self):
        for teacher in self.teachers:
            self.school_system.add_teacher(teacher)
            self.assertIn(teacher, self.school_system.teachers)

    def test_add_invalid_teacher(self):
        invalid_teacher = Teacher(first_name="Anna", last_name="Smith", birth_date=datetime(2005, 7, 20),
                                  subjects=["History"])
        with self.assertRaises(TeachersAgeException):
            self.school_system.add_teacher(invalid_teacher)

    def test_assign_teachers_to_student(self):
        self.add_teachers()
        self.school_system.add_student(self.student)

        expected_subjects = set(self.school_system.junior_subjects)

        self.assertEqual(len(self.student.teachers), len(expected_subjects))

    def test_no_suitable_teacher(self):
        with self.assertRaises(NoSuitableTeacherException):
            self.school_system.add_student(self.student)

    def test_fire_teachers_without_students(self):
        teacher = Teacher(
            "Александр", "Соколов",
            datetime.strptime("25-03-1985", '%d-%m-%Y'),
            ["Русский язык", "Биология"]
        )
        self.school_system.add_teacher(teacher)
        with patch('builtins.input', return_value='да'):
            self.school_system.fire_teachers_without_students(confirm=True)
        self.assertNotIn(teacher, self.school_system.teachers)

    @patch("builtins.open", new_callable=MagicMock)
    def test_export_class_list(self, mock_open):
        self.add_teachers()
        self.school_system.add_student(self.student)
        self.school_system.export_class_list(5)

        mock_open.assert_called_once_with("class_5_list.txt", "w", encoding="utf-8")


if __name__ == '__main__':
    unittest.main()
