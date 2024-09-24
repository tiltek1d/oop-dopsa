from dataclasses import dataclass, field
from random import choice

from .student import Student
from .teacher import Teacher
from ..exceptions import StudentsAgeException, TeachersAgeException, NoSuitableTeacherException


@dataclass
class SchoolSystem:
    verbose: bool = True

    students: list[Student] = field(default_factory=list)
    teachers: list[Teacher] = field(default_factory=list)

    junior_subjects: tuple[str] = ("Математика", "Русский язык", "Науки о природе")
    senior_subjects: tuple[str] = (
        "Математика", "Русский язык", "Науки о природе",
        "Физика", "Химия", "Информатика", "Биология",
    )

    def add_student(self, student: Student):
        if student.is_valid_student:
            self.students.append(student)
            self.assign_teachers_to_student(student)
            self.print_teachers_without_students()
        else:
            raise StudentsAgeException(
                f"Ученик {student.first_name} {student.last_name} старше 18 лет и не может учиться в школе."
            )

    def add_teacher(self, teacher: Teacher):
        if teacher.is_valid_teacher:
            self.teachers.append(teacher)
        else:
            raise TeachersAgeException(
                f"Учитель {teacher.first_name} {teacher.last_name} не соответствует возрастным ограничениям."
            )

    @staticmethod
    def cross_assign_teacher_and_student(teacher: Teacher, student: Student):
        teacher.assign_student(student)
        student.assign_teacher(teacher)

    def assign_teachers_to_student(self, student: Student):
        required_subjects = self.junior_subjects if student.grade < 7 else self.senior_subjects
        assigned_teachers = []

        for subject in required_subjects:
            available_teachers = [teacher for teacher in self.teachers if subject in teacher.subjects]

            if available_teachers:
                selected_teacher = choice(available_teachers)
                self.cross_assign_teacher_and_student(selected_teacher, student)
                assigned_teachers.append((subject, selected_teacher))
            else:
                raise NoSuitableTeacherException(
                    f"Для предмета {subject} нет учителя для ученика {student.first_name} {student.last_name}"
                )

        if self.verbose:
            print(f"Ученику {student.first_name} {student.last_name} назначены следующие учителя:")
            for subject, teacher in assigned_teachers:
                print(f"Предмет: {subject} -> Учитель: {teacher.first_name} {teacher.last_name}")

    def print_teachers_without_students(self):
        no_student_teachers = [teacher for teacher in self.teachers if not teacher.students]
        print(f"Учителей без учеников: {len(no_student_teachers)}")

    def fire_teachers_without_students(self, confirm: bool = True):
        no_student_teachers = [teacher for teacher in self.teachers if not teacher.students]
        if no_student_teachers:
            if self.verbose:
                print(f"Следующие учителя не имеют учеников:")
                for teacher in no_student_teachers:
                    print(f"{teacher.first_name} {teacher.last_name}, предметы: {', '.join(teacher.subjects)}")

                if confirm:
                    firing_confirmed = True if input(
                        "Хотите уволить этих учителей? (да/нет): ").strip().lower() == 'да' else False
                else:
                    firing_confirmed = True
            else:
                firing_confirmed = True

            if firing_confirmed:
                for teacher in no_student_teachers:
                    self.teachers.remove(teacher)
                if self.verbose:
                    print("Учителя без учеников уволены.")
            else:
                if self.verbose:
                    print("Учителя не были уволены.")
        else:
            if self.verbose:
                print("Все учителя имеют учеников.")

    def export_class_list(self, grade: int):
        filename = f"class_{grade}_list.txt"
        with open(filename, "w", encoding="utf-8") as file:
            for student in self.students:
                if student.grade == grade:
                    file.write(f"{student}\n")
                    for teacher in student.teachers:
                        file.write(
                            f"\tУчитель: {teacher.first_name} {teacher.last_name}, Предмет: {', '.join(teacher.subjects)}\n")
        print(f"Список класса {grade} экспортирован в файл {filename}.")
