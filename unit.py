__author__ = 'nice'

import unittest

class UnitIsDeadError(Exception):
    pass

class Unit:
    def __init__(self, name='unit', hit_points_limit=100, hit_points=100, damage=10):
        self.name = name
        self.hit_points_limit = hit_points
        self.hit_points = hit_points
        self.damage = damage

    def __str__(self):
        return '--------------------\nName: {}\nDamage: {}\nHit Points: {}\nHit points limit: {}\n--------------------\n'.format(self.name, self.damage, self.hit_points, self.hit_points_limit)

    def ensure_is_alive(self):
        if self.hit_points == 0:
            raise UnitIsDeadError('Unit is dead')

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
        self.assertRaises(UnitIsDeadError(), soldier.ensure_is_alive())

    def test_add_hit_points(self):
        soldier = Unit('Soldier', 100, 10, 10)
        self.assertEqual(soldier.hit_points, 10)
        
        i = 10
        while i < soldier.hit_points_limit:
            soldier.add_hit_points(soldier.damage)
            i += 10
            self.assertEqual(soldier.hit_points, i)

        self.assertEqual(soldier.hit_points, 100)
        self.assertEqual(soldier.hit_points, 100)

if __name__ == '__main__':
    unittest.main()

# soldier = Unit('soldier')
# warior = Unit('warior')

# print(soldier)
# print(warior)

# soldier.attack(warior)

# print(soldier)
# print(warior)