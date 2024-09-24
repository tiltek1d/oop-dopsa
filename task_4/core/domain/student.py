from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .person import Person

if TYPE_CHECKING:
    from .teacher import Teacher


@dataclass
class Student(Person):
    grade: int
    teachers: list['Teacher'] = field(default_factory=list)

    @property
    def is_valid_student(self) -> bool:
        return self.age < 18

    def assign_teacher(self, teacher: 'Teacher'):
        self.teachers.append(teacher)

    def __str__(self) -> str:
        return f"Ученик {self.first_name} {self.last_name}, Класс: {self.grade}, Возраст: {self.age}"
