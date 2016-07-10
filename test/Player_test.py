import unittest
from Player import Player
from Race_tech_tree import Humans
from Humans_peasant import Peasant
from Barracks import Barracks
from Humans_Townhall import HumansTownhall,Castle
from Footman import Footman
from Knight import Knight

class TestStringMethods(unittest.TestCase):

    def test_choose_race(self):
        player1 = Player('Humans','p1')
        self.assertEqual(player1.race,'Humans')


    def test_create_unit(self):
        player1 = Player('Humans', 'p1')
        self.assertEqual(len(player1.unit_list),0)
        self.assertEqual(len(player1.tech_tree_list),0)
        player1.create_unit(Peasant)
        list = []
        for unit in player1.unit_list:
            list.append(unit[:7])
        self.assertEqual(list,['peasant'])
        self.assertEqual(player1.tech_tree_list,['peasant'])


    def test_check_tech_tree_in_townhall(self):
        townhall = HumansTownhall()
        self.assertEqual(len(townhall.check_tech_tree_in_townhall(Peasant)), 0)

    def test_creat_unit_in_townhall(self):
        player1 = Player('Humans', 'p1')
        townhall = HumansTownhall()
        townhall.owner = player1
        townhall.creat_unit_in_townhall(Peasant)
        list = []
        for unit in player1.unit_list:
            list.append(unit[:7])
        self.assertEqual(list, ['peasant'])

    def test_creat_unit_in_barracks(self):
        player1 = Player('Humans', 'p1')
        barracks = Barracks()
        barracks.owner = player1
        self.assertEqual(player1.tech_tree_list, [])
        barracks.creat_unit_in_barracks(Footman)
        player1.create_unit(Peasant)
        self.assertEqual(player1.tech_tree_list,['footman','peasant'])
        list = []
        for unit in player1.unit_list:
            list.append(unit[:7])
        self.assertEqual(list, ['footman','peasant'])
        barracks.creat_unit_in_barracks(Knight)
        list = []
        for unit in player1.unit_list:
            list.append(unit[:7])
        self.assertEqual(list, ['footman','peasant'])
        player1.create_unit(Castle)
        barracks.creat_unit_in_barracks(Knight)
        list = []
        for unit in player1.unit_list:
            list.append(unit[:6])
        self.assertEqual(list, ['footma','peasan','castle','knight'])


if __name__ == '__main__':
    unittest.main()