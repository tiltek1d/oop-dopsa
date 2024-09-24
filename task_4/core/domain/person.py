from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: datetime

    @property
    def age(self) -> int:
        today = datetime.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
