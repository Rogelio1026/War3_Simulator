import unittest
from Player import Player
from Race_tech_tree import Humans
from Humans_peasant import Peasant

class TestStringMethods(unittest.TestCase):

    def test_choose_race(self):
        player1 = Player('Humans','p1')
        print(player1.my_race,Humans(),player1.my_race.unit_class_list)

    def test_create_unit(self):
        player1 = Player('Humans', 'p1')
        player1.create_unit(Peasant)
        print(player1.unit_list)





if __name__ == '__main__':
    unittest.main()