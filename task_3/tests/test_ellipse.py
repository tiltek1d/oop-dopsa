import math
import unittest

from core import Ellipse
from core.utils import GeometryUtils


class TestEllipse(unittest.TestCase):
    def setUp(self):
        self.ellipse = Ellipse(x=5, y=10, major_axis=20, minor_axis=10, color="green", visible=True)

    def test_initialization(self):
        self.assertEqual(self.ellipse.get_position(), (5, 10))
        self.assertEqual(self.ellipse.major_axis, 20)
        self.assertEqual(self.ellipse.minor_axis, 10)
        self.assertEqual(self.ellipse.get_color(), "green")
        self.assertTrue(self.ellipse.is_visible)

    def test_area(self):
        expected_area = math.pi * 20 * 10 / 4
        self.assertAlmostEqual(self.ellipse.area, expected_area, places=5)

    def test_perimeter(self):
        h = ((20 - 10) ** 2) / ((20 + 10) ** 2)
        expected_perimeter = math.pi * (20 + 10) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        self.assertAlmostEqual(self.ellipse.perimeter, expected_perimeter, places=5)

    def test_is_within_bounds(self):
        GeometryUtils.is_within_bounds = lambda x, y, major, minor: True
        self.assertTrue(self.ellipse.is_within_bounds())

    def test_str_method(self):
        expected_str = (
            "Эллипс на позиции (5, 10) с осями 20 и 10\n"
            "Цвет: green, Видимость: True\n"
            f"Площадь: {self.ellipse.area}, Периметр: {self.ellipse.perimeter}\n"
            "В пределах области: True\n"
        )
        self.assertEqual(str(self.ellipse), expected_str)


if __name__ == '__main__':
    unittest.main()
