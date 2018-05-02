__author__ = 'nice'

from math import hypot
from point import Point
import unittest

class NotEnoughFuelException(Exception):
    """A class for exceptions."""
    pass


class Car:
    """
    A class for Car representing.
    Use types: string, integer, Point().

    Usage:
    >>> car = Car()
    >>> print(car)
    Model: car
    Location: (0, 0)
    >>> destination = Point(0, 10)
    >>> car.drive(destination)
    >>> print(car)
    Model: car
    Location: (0, 10)
    """

    def __init__(self, model='car', fuel_amount=10, fuel_capacity=100,
                 fuel_consumption=5, location=Point(0, 0)):
        """
        The initializer.

        :param model: Possible values: string.
        :param fuel_amount: Possible values: integer, float.
        :param fuel_capacity: Possible values: integer, float.
        :param fuel_consumption: Possible values: integer, float.
        :param location: Possible values: Point().
        """

        self._model = model
        self._fuel_amount = fuel_amount if fuel_amount <= fuel_capacity else fuel_capacity
        self._fuel_capacity = fuel_capacity
        self._fuel_consumption = fuel_consumption
        self._location = location

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def fuel_amount(self):
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        self._fuel_amount = value

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value):
        self._fuel_capacity = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self._fuel_consumption = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def __str__(self):
        return 'Model: {}\nLocation: {}'.format(self.model, self.location)

    def validate(self, destination):
        """
        Fuel amount validator.
        
        :param destination: Destination location to validate.
        :type destination: Point.
        :rtype: bool.
        :return: validate status.
        """

        return self.fuel_amount >= self.location.distance(destination) * self.fuel_consumption

    def refill(self, amount=100):
        """
        Refills car fuel tank.

        :param amount: amount of fuel for refueling.
        :type amount: integer, float.
        """

        if amount > self.fuel_capacity - self.fuel_amount:
            self.fuel_amount = self.fuel_capacity
        else:
            self.fuel_amount += amount

    def drive(self, destination):
        """
        Drives car. Changes current location to destination.

        :param destination: location to move.
        :type destination: Point.
        :raise NotEnoughFuelException: If not enough fuel to reach the required location.
        """

        if not self.validate(destination):
            raise NotEnoughFuel('Not enough fuel')
        self.fuel_amount -= self.location.distance(destination) * self.fuel_consumption
        self.location = destination            

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
        self.assertRaises(NotEnoughFuelException(), bmw.drive(Point(30, 30)))

if __name__ == '__main__':
    unittest.main()