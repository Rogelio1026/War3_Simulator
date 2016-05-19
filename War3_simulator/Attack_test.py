from Humans_peasant import Peasant
from Orcs_peon import Peon
from Humans_Townhall import HumansTownhall
import unittest
class TestStringMethods(unittest.TestCase):
    def test_under_attacked(self):
        peasant = Peasant()
        self.assertEqual(peasant.max_hp,220)
        self.assertEqual(peasant.attack_type,'normal attack')
        self.assertEqual(peasant.damage,10)
        peasant.underattacked(100)
        self.assertEqual(peasant.current_hp, 120)
        self.assertEqual(peasant.alive(), True)
        peasant.underattacked(150)
        self.assertEqual(peasant.current_hp, 0)
        self.assertEqual(peasant.alive(), False)

    def test_attack(self):
        peon = Peon()
        humanstownhall = HumansTownhall()
        humanstownhall.underattacked(peon.damage)
        self.assertEqual(humanstownhall.current_hp, 1490)
        while humanstownhall.current_hp > 0:
            humanstownhall.current_hp = humanstownhall.current_hp - peon.damage
        self.assertEqual(humanstownhall.alive(), False)
if __name__ == '__main__':
    unittest.main()