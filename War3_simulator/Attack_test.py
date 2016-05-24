from Humans_peasant import Peasant
from Orcs_peon import Peon
from Humans_Townhall import HumansTownhall
import unittest
class TestStringMethods(unittest.TestCase):
    def test_under_attacked(self):
        peasant = Peasant()
        self.assertEqual(peasant.max_hp,220)
        self.assertEqual(peasant.armor_type, 'light')
        self.assertEqual(peasant.attack,5.5)
        peasant.underattacked(10, 'pierce')
        print(peasant.damage_change)
        self.assertEqual(peasant.current_hp, 200)
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
if __name__ == '__main__':
    unittest.main()