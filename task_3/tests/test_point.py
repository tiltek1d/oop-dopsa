import unittest

from core.point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(x=5, y=10, color="red", visible=True)

    def test_initialization(self):
        self.assertEqual(self.point.get_position(), (5, 10))
        self.assertEqual(self.point.get_color(), "red")
        self.assertTrue(self.point.is_visible)

    def test_str_method(self):
        expected_str = "Точка на позиции (5, 10) с цветом red и видимостью True"
        self.assertEqual(str(self.point), expected_str)

    def test_set_position(self):
        self.point.set_position(15, 20)
        self.assertEqual(self.point.get_position(), (15, 20))

    def test_set_color(self):
        self.point.set_color("blue")
        self.assertEqual(self.point.get_color(), "blue")

    def test_set_visibility(self):
        self.point.set_visibility(False)
        self.assertFalse(self.point.is_visible)


if __name__ == '__main__':
    unittest.main()
