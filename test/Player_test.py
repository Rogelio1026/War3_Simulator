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
        print(player1.unit_list,1)
        print(player1.tech_tree_list,2)


    def test_check_tech_tree_in_townhall(self):
        townhall = HumansTownhall()
        print (townhall.check_tech_tree_in_townhall(Peasant),3)

    def test_creat_unit_in_townhall(self):
        player1 = Player('Humans', 'p1')
        townhall = HumansTownhall()
        townhall.owner = player1
        townhall.creat_unit_in_townhall(Peasant)
        print(player1.unit_list, 4)

    def test_creat_unit_in_barracks(self):
        player1 = Player('Humans', 'p1')
        barracks = Barracks()
        barracks.owner = player1
        print(player1.tech_tree_list, 5)
        barracks.creat_unit_in_barracks(Footman)
        player1.create_unit(Peasant)
        # player1.tech_tree_list = ['peasant']
        barracks.creat_unit_in_barracks(Footman)
        print(player1.unit_list, 6)
        barracks.creat_unit_in_barracks(Knight)
        print(player1.unit_list, 7)
        player1.create_unit(Castle)
        barracks.creat_unit_in_barracks(Knight)
        print(player1.unit_list, 8)


if __name__ == '__main__':
    unittest.main()