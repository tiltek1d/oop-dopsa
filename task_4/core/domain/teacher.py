from dataclasses import dataclass, field

from .person import Person
from .student import Student


@dataclass
class Teacher(Person):
    subjects: list[str]
    students: list[Student] = field(default_factory=list)

    @property
    def is_valid_teacher(self) -> bool:
        return 27 <= self.age <= 70

    def assign_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self) -> str:
        return f"Учитель {self.first_name} {self.last_name}, Предметы: {', '.join(self.subjects)}, Возраст: {self.age}"
