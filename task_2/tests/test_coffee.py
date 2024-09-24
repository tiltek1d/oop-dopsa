import unittest

from core.coffee import Coffee


class TestCoffee(unittest.TestCase):
    def test_order_with_sugar_and_syrup(self):
        coffee = Coffee(coffee_type="Латте", sugar=True, syrup="Ванильный")
        self.assertEqual(coffee.get_order_info(), "Вы выбрали Латте, с сахаром, с сиропом Ванильный.")

    def test_order_with_sugar_no_syrup(self):
        coffee = Coffee(coffee_type="Американо", sugar=True, syrup="")
        self.assertEqual(coffee.get_order_info(), "Вы выбрали Американо, с сахаром, без сиропа.")

    def test_order_no_sugar_with_syrup(self):
        coffee = Coffee(coffee_type="Капучино", sugar=False, syrup="Шоколадный")
        self.assertEqual(coffee.get_order_info(), "Вы выбрали Капучино, без сахара, с сиропом Шоколадный.")

    def test_order_no_sugar_no_syrup(self):
        coffee = Coffee(coffee_type="Эспрессо", sugar=False, syrup="")
        self.assertEqual(coffee.get_order_info(), "Вы выбрали Эспрессо, без сахара, без сиропа.")


if __name__ == '__main__':
    unittest.main()
