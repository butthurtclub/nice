__author__ = 'nice'

from math import hypot
import unittest

__all__ = (
    'Point',
)

class Point:
    def __init__(self, first_arg=0, second_arg=0):
        self.x = first_arg
        self.y = second_arg
    def distance(self, other):
        return hypot(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x and self.y != other.y
    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class PointTest(unittest.TestCase):
    def test_initial(self):
        first = Point(4, 7)
        self.assertIsInstance(first, Point)
        self.assertEqual(first.x, 4)
        self.assertEqual(first.y, 7)
        self.assertEqual((first.x, first.y), (4, 7))

    def test_distance(self):
        first = Point(0, 0)
        second = Point(0, 2)
        self.assertEqual(first.distance(second), 2)

    def test_equal(self):
        first = Point(1, 2)
        second = Point(1, 2)
        self.assertEqual(first, second)

    def test_not_equal(self):
        first = Point(2, 3)
        second = Point(1, 2)
        self.assertNotEqual(first, second)


if __name__ == '__main__':
    unittest.main()