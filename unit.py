__author__ = 'nice'

import unittest

class UnitIsDeadException(Exception):
    pass

class Unit:
    def __init__(self, name='unit', hit_points_limit=100, hit_points=100, damage=10):
        self.name = name
        self.hit_points_limit = hit_points
        self.hit_points = hit_points
        self.damage = damage

    def __str__(self):
        return 'Name: {}\nDamage: {}\nHit Points: {}\n'.format(self.name, self.damage, self.hit_points)

    def ensure_is_alive(self):
        if self.hit_points == 0:
            raise UnitIsDeadException('Unit is dead')

    def add_hit_points(self, hp):
        self.ensure_is_alive()

        if hp >= self.hit_points_limit - self.hit_points:
            self.hit_points = self.hit_points_limit
        else:
            self.hit_points += hp

    def take_damage(self, dmg):
        self.ensure_is_alive()

        if dmg > self.hit_points:
            self.hit_points = 0
        else:
            self.hit_points -= dmg

    def attack(self, enemy):
        enemy.ensure_is_alive()

        enemy.take_damage(self.damage)
        enemy.counter_attack(self)

    def counter_attack(self, enemy):
        enemy.ensure_is_alive()

        enemy.take_damage(self.damage/2)

class UnitTest(unittest.TestCase):
    def test_initial(self):
        soldier = Unit('Soldier', 100, 100, 10)

        self.assertIsInstance(soldier, Unit)
        self.assertEqual(soldier.name, 'Soldier')
        self.assertEqual(soldier.hit_points_limit, 100)
        self.assertEqual(soldier.hit_points, 100)
        self.assertEqual(soldier.damage, 10)

    def test_ensure_is_alive(self):
        soldier = Unit()

        self.assertRaises(UnitIsDeadException(), soldier.ensure_is_alive())

    def test_add_hit_points(self):
        soldier = Unit('Soldier', 100, 100, 10)

        self.assertEqual(soldier.hit_points, 100)
        soldier.take_damage(30)
        self.assertEqual(soldier.hit_points, 70)
        soldier.add_hit_points(500)
        self.assertEqual(soldier.hit_points, 100)

    def test_take_damage(self):
        soldier = Unit('Soldier', 100, 100, 10)

        self.assertEqual(soldier.hit_points, 100)
        soldier.take_damage(30)
        self.assertEqual(soldier.hit_points, 70)
        soldier.take_damage(30)
        self.assertEqual(soldier.hit_points, 40)
        soldier.take_damage(30)
        self.assertEqual(soldier.hit_points, 10)
        self.assertRaises(UnitIsDeadException(), soldier.take_damage(30))

    def test_counter_attack(self):
        soldier = Unit('Soldier', 100, 100, 10)
        knight = Unit('Knight', 150, 150, 10)

        self.assertEqual(soldier.hit_points, 100)
        self.assertEqual(knight.hit_points, 150)
        soldier.attack(knight)
        self.assertEqual(soldier.hit_points, 95)
        self.assertEqual(knight.hit_points, 140)
        knight.attack(soldier)
        self.assertEqual(soldier.hit_points, 85)
        self.assertEqual(knight.hit_points, 135)

if __name__ == '__main__':
    unittest.main()