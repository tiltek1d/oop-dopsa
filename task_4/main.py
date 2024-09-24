from datetime import datetime

from core import SchoolSystem, Student, Teacher, StudentsAgeException


def add_students_from_input(school: SchoolSystem, num_students: int) -> None:
    i = 1
    while i <= num_students:
        print(i, num_students)
        first_name = input(f"Введите имя ученика {i}: ")
        last_name = input(f"Введите фамилию ученика {i}: ")
        birth_date_str = input(f"Введите дату рождения ученика {i} (дд-мм-гггг): ")
        birth_date = datetime.strptime(birth_date_str, '%d-%m-%Y')
        grade = int(input(f"Введите класс ученика {i}: "))
        student = Student(first_name, last_name, birth_date, grade)
        try:
            school.add_student(student)
            print(f"Ученик {first_name} {last_name} добавлен.\n")
            i += 1
        except StudentsAgeException as e:
            print(e)

    school.fire_teachers_without_students()


def main():
    school = SchoolSystem()

    teacher1 = Teacher("Светлана", "Смирнова", datetime.strptime("15-06-1980", '%d-%m-%Y'),
                       ["Математика", "Русский язык"])
    teacher2 = Teacher("Ольга", "Кузнецова", datetime.strptime("10-02-1975", '%d-%m-%Y'),
                       ["Физика", "Информатика", "Науки о природе"])
    teacher3 = Teacher("Иван", "Попов", datetime.strptime("20-09-1990", '%d-%m-%Y'),
                       ["Химия", "Биология", "Науки о природе"])
    teacher4 = Teacher("Александр", "Соколов", datetime.strptime("25-03-1985", '%d-%m-%Y'),
                       ["Русский язык", "Биология"])
    teacher5 = Teacher("Мария", "Лебедева", datetime.strptime("30-07-1978", '%d-%m-%Y'), ["Физика", "Информатика"])

    for teacher in [teacher1, teacher2, teacher3, teacher4, teacher5]:
        school.add_teacher(teacher)

    add_students_from_input(school, 2)

    school.export_class_list(10)


if __name__ == '__main__':
    main()
