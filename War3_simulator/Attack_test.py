from Humans_peasant import Peasant
from Orcs_peon import Peon
from Humans_Townhall import HumansTownhall
from clock import Game
from clock import Player
from Unit import Unit
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
        peon = Peon()
        humanstownhall = HumansTownhall()
        self.assertEqual(humanstownhall.current_hp, 1500)
        humanstownhall.underattacked(peon.attack, peon.attack_type)
        self.assertEqual(humanstownhall.current_hp, 1494.75)
        while humanstownhall.current_hp > 0:
            humanstownhall.underattacked(peon.attack, peon.attack_type)
        self.assertEqual(humanstownhall.alive(), False)

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


    def hpRegnerate(self):
        game = Game()
        player1 = Player('Human')
        peasant = Peasant()
        player1.add_units(peasant)
        self.assertEqual(peasant.max_hp, 220)
        self.assertEqual(peasant.armor_type, 'light')
        self.assertEqual(peasant.attack, 5.5)
        peasant.underattacked(50, 'pierce')
        self.assertEqual(peasant.current_hp, 120)
        self.assertEqual(peasant.alive(), True)
        player1.clock(24)
        self.assertEqual(peasant.current_hp, 144)
        peasant.underattacked(250, 'hero')
        player1.clock(24)
        self.assertEqual(peasant.current_hp, 0)
        self.assertEqual(peasant.alive(), False)

if __name__ == '__main__':
    unittest.main()