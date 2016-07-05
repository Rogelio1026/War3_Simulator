import unittest
from Player import Player
from Race_tech_tree import Humans
from Humans_peasant import Peasant
from Barracks import Barracks
from Humans_Townhall import HumansTownhall

class TestStringMethods(unittest.TestCase):

    def test_choose_race(self):
        player1 = Player('Humans','p1')


    def test_create_unit(self):
        player1 = Player('Humans', 'p1')
        player1.create_unit(Peasant)
        print(player1.unit_list)


    def test_check_tech_tree_in_townhall(self):
        townhall = HumansTownhall()
        print (townhall.check_tech_tree_in_townhall(Peasant))

    def test_creat_unit_in_townhall(self):
        player1 = Player('Humans', 'p1')
        townhall = HumansTownhall()
        townhall.owner = player1
        townhall.creat_unit_in_townhall(Peasant)
        print(player1.unit_list,1)



if __name__ == '__main__':
    unittest.main()