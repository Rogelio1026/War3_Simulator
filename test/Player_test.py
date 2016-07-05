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
        player1.create_unit(Barracks)

    # def




if __name__ == '__main__':
    unittest.main()