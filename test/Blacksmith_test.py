import unittest
from Player import Player
from Humans_peasant import Peasant
from Blacksmith import Blacksmith
from Humans_Townhall import HumansTownhall,Castle

class TestStringMethods(unittest.TestCase):

    def test_check_tech_tree_in_blacksmith(self):
        blacksmith = Blacksmith()
        self.assertEqual(blacksmith.check_tech_tree_in_blacksmith('melee_attack_l2'),['keep'])

    def test_upgrade_in_black_smith(self):
        player1 = Player('Humans', 'p1')
        blacksmith = Blacksmith()
        blacksmith.owner = player1
        blacksmith.upgrade_in_black_smith('melee_attack_l2')

if __name__ == '__main__':
    unittest.main()