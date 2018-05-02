__author__ = 'nice'

from math import hypot
from point import *
import unittest

class NotEnoughFuel(Exception):
    pass


class Car:
    def __init__(self, model='car', fuel_amount=10, fuel_capacity=100,
                 fuel_consumption=5, location=Point(0, 0)):
        self.model = model
        self.fuel_amount = fuel_amount if fuel_amount <= fuel_capacity else fuel_capacity
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.location = location

    def __str__(self):
        return 'Model: {}\nLocation: {}'.format(self.model, self.location)

    def validate(self, destination):
        if self.fuel_amount >= self.location.distance(destination) * self.fuel_consumption:
            return True
        else:
            return False

    def refill(self, amount=100):
        if amount > self.fuel_capacity - self.fuel_amount:
            self.fuel_amount = self.fuel_capacity
        else:
            self.fuel_amount += amount

    def drive(self, destination):
        if self.validate(destination):
            self.fuel_amount -= self.location.distance(destination) * self.fuel_consumption
            self.location = destination
        else:
            raise NotEnoughFuel('Not enough fuel')

class CarTest(unittest.TestCase):
    def test_initial(self):
        bmw = Car('BMW', 60, 80, 9, Point(0, 0))
        self.assertIsInstance(bmw, Car)
        self.assertEqual(bmw.model, 'BMW')
        self.assertEqual(bmw.fuel_amount, 60)
        self.assertEqual(bmw.fuel_capacity, 80)
        self.assertEqual(bmw.fuel_consumption, 9)
        self.assertEqual(bmw.location, Point(0, 0))

    def test_validate(self):
        bmw = Car('BMW', 60, 80, 9, Point(5, 5))
        self.assertTrue(bmw.validate(Point(7, 7)))
        self.assertFalse(bmw.validate(Point(15, 15)))

    def test_refill(self):
        bmw = Car('BMW', 60, 80, 9, Point(0, 0))
        self.assertEqual(bmw.fuel_amount, 60)
        bmw.refill(50)
        self.assertEqual(bmw.fuel_amount, 80)

    def test_drive(self):
        bmw = Car('BMW', 60, 80, 1, Point(0, 0))
        self.assertEqual(bmw.fuel_amount, 60)
        bmw.drive(Point(0, 10))
        self.assertEqual(bmw.location, Point(0, 10))
        self.assertEqual(bmw.fuel_amount, 50)
        bmw.drive(Point(10, 10))
        self.assertEqual(bmw.location, Point(10, 10))
        self.assertEqual(bmw.fuel_amount, 40)
        self.assertRaises(NotEnoughFuel(), bmw.drive(Point(30, 30)))

if __name__ == '__main__':
    unittest.main()