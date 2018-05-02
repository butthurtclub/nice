__author__ = 'nice'

from math import hypot
import unittest

class Car:
    def __init__(self, model='car', fuel_amount=10, fuel_capacity=100,
                 fuel_consumption=5, location_x=0, location_y=0):
        self.model = model
        self.fuel_amount = fuel_amount if fuel_amount <= fuel_capacity else fuel_capacity
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.x = location_x
        self.y = location_y

    def __str__(self):
        return '--------------------\nModel: {}\nFuel amount: {}\nFuel capacity: {}\nFuel consumption: {}\nLocation: ({}, {})\n--------------------\n'.format(self.model, self.fuel_amount, self.fuel_capacity, self.fuel_consumption, self.x, self.y)

    def validate(self, destination_x, destination_y):
        if self.fuel_amount >= hypot(self.x - destination_x, self.y - destination_y) * self.fuel_consumption:
            return True
        else:
            return False

    def refill(self, amount=100):
        if amount > self.fuel_capacity - self.fuel_amount:
            self.fuel_amount = self.fuel_capacity
        else:
            self.fuel_amount += amount

    def drive(self, destination_x, destination_y):
        if self.validate(destination_x, destination_y):
            self.fuel_amount -= hypot(self.x - destination_x, self.y - destination_y) * self.fuel_consumption
            self.x = destination_x
            self.y = destination_y
        else:
            print('Not enough fuel')

class CarTest(unittest.TestCase):
    def test_initial(self):
        bmw = Car('BMW', 60, 80, 9, 0, 0)
        self.assertIsInstance(bmw, Car)
        self.assertEqual(bmw.model, 'BMW')
        self.assertEqual(bmw.fuel_amount, 60)
        self.assertEqual(bmw.fuel_capacity, 80)
        self.assertEqual(bmw.fuel_consumption, 9)
        self.assertEqual(bmw.x, 0)
        self.assertEqual(bmw.y, 0)

    def test_validate(self):
        bmw = Car('BMW', 60, 80, 9, 5, 5)
        self.assertTrue(bmw.validate(7, 7))
        self.assertFalse(bmw.validate(15, 15))

    def test_refill(self):
        bmw = Car('BMW', 60, 80, 9, 0, 0)
        self.assertEqual(bmw.fuel_amount, 60)
        bmw.refill(50)
        self.assertEqual(bmw.fuel_amount, 80)

    def test_drive(self):
        bmw = Car('BMW', 60, 80, 1, 0, 0)
        self.assertEqual(bmw.fuel_amount, 60)
        bmw.drive(0, 10)
        self.assertEqual(bmw.x, 0)
        self.assertEqual(bmw.y, 10)
        self.assertEqual(bmw.fuel_amount, 50)
        bmw.drive(10, 10)
        self.assertEqual(bmw.x, 10)
        self.assertEqual(bmw.y, 10)
        self.assertEqual(bmw.fuel_amount, 40)
        
if __name__ == '__main__':
    unittest.main()