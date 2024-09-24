import unittest

from core.basics import Position, GeometricPrimitive, BoundingBox


class TestPosition(unittest.TestCase):
    def setUp(self):
        self.position = Position(x=5, y=10)

    def test_get_position(self):
        self.assertEqual(self.position.get_position(), (5, 10))

    def test_set_position(self):
        self.position.set_position(15, 20)
        self.assertEqual(self.position.get_position(), (15, 20))


class TestBoundingBox(unittest.TestCase):
    def setUp(self):
        self.bounding_box = BoundingBox(width=50, height=100)

    def test_get_bounding_box(self):
        self.assertEqual(self.bounding_box.get_bounding_box(), (50, 100))

    def test_negative_dimensions(self):
        bounding_box = BoundingBox(width=-10, height=-20)
        self.assertEqual(bounding_box.get_bounding_box(), (-10, -20))


class TestGeometricPrimitive(unittest.TestCase):
    def setUp(self):
        self.primitive = GeometricPrimitive()

    def test_default_values(self):
        self.assertEqual(self.primitive.get_color(), 'black')
        self.assertTrue(self.primitive.is_visible)

    def test_set_color(self):
        self.primitive.set_color('red')
        self.assertEqual(self.primitive.get_color(), 'red')

    def test_set_visibility(self):
        self.primitive.set_visibility(False)
        self.assertFalse(self.primitive.is_visible)
        self.primitive.set_visibility(True)
        self.assertTrue(self.primitive.is_visible)


if __name__ == '__main__':
    unittest.main()
