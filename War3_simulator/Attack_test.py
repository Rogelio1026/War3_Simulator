from Humans_peasant import Peasant
from Orcs_peon import Peon
from Humans_Townhall import HumansTownhall
from clock import Game
from Unit import Unit
# from library import compareDoubles
import unittest
class TestStringMethods(unittest.TestCase):
    def test_under_attacked(self):
        peasant = Peasant()
        self.assertEqual(peasant.max_hp,220)
        self.assertEqual(peasant.armor_type, 'light')
        peasant.underattacked(50, 'pierce')
        self.assertEqual(peasant.current_hp, 120)
        self.assertEqual(peasant.alive(), True)
        peasant.underattacked(250, 'hero')
        self.assertEqual(peasant.current_hp, 0)
        self.assertEqual(peasant.alive(), False)

    def test_attack(self):
        peasant = Peasant()
        peon = Peon()
        self.assertEqual(peon.current_hp, 250)
        print(callable(peon))
        peasant.attack(peon)
        self.assertEqual(peon.current_hp, 1494.75)
        while peon.current_hp > 0:
            peon.underattacked(peasant.attack, peasant.attack_type)
        self.assertEqual(peon.alive(), False)

    def test_damage_change_lookup(self):
        unit = Unit()
        damage_change = unit.damage_change_lookup('siege','hero')
        self.assertEqual(damage_change, .5)
        damage_change = unit.damage_change_lookup('hero', 'heavy')
        self.assertEqual(damage_change, 1)

    def test_damage_soak(self):
        unit = Unit()
        damage_change = unit.damage_soak(0)
        self.assertEqual(damage_change, 1)

    def test_alive(self):
        unit = Unit()
        unit.underattacked(100,'chaos')
        self.assertEqual(unit.current_hp, 0)

    def test_hpRegnerate(self):
        game = Game()
        peasant = Peasant()
        game.add_recipients(peasant)
        self.assertEqual(peasant.max_hp, 220)
        self.assertEqual(peasant.armor_type, 'light')
        self.assertEqual(peasant.hp_regeneration_rate, 1)
        peasant.underattacked(50, 'pierce')
        self.assertEqual(peasant.current_hp, 120)
        self.assertEqual(peasant.alive(), True)
        count = 0
        t = 24
        while count < t:
            game.clock()
            count += 1
        self.assertEqual(round(peasant.current_hp), 121.0)
        peasant.underattacked(250, 'hero')
        self.assertEqual(peasant.alive(), False)
        count = 0
        t = 24
        while count < t:
            game.clock()
            count += 1
        self.assertEqual(peasant.current_hp, 0)
        self.assertEqual(peasant.alive(), False)
        # peasant.comparDoubles(1,2,1)
if __name__ == '__main__':
    unittest.main()