__author__ = 'nice'

from math import hypot
import unittest

__all__ = (
    'Point',
)

class Point:
    """
    A class for Point(x,y) representing.
    Supported types: integer, floating.

    Usage:
    >>> first = Point()
    >>> first
    (0, 0)
    >>> second = Point(0, 2)
    >>> second
    (0, 2)
    >>> first.distance(second)
    2.0
    >>> first == second
    False
    >>> first = second
    >>> first == second
    >>> True
    """

    def __init__(self, x=0, y=0):
        """
        The initializer.

        :param x: x-coordinate. Possible values: integer, float.
        :param y: y-coordinate. Possible values: integer, float. 
        """
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def distance(self, other):
        """
        Counts distance between two points.
        :param other: Point.
        :return: float.
        """

        return hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

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

first = Point()
second = Point(0, 2)
print(first)
print(second)
print(first.distance(second))

if __name__ == '__main__':
    unittest.main()