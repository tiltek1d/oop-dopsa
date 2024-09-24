from dataclasses import dataclass


@dataclass
class Coffee:
    coffee_type: str
    sugar: bool
    syrup: str

    def get_order_info(self):
        sugar_info = "с сахаром" if self.sugar else "без сахара"
        syrup_info = f"с сиропом {self.syrup}" if self.syrup else "без сиропа"
        return f"Вы выбрали {self.coffee_type}, {sugar_info}, {syrup_info}."
