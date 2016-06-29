import unittest
from Player import Player
from Race_tech_tree import Humans

class TestStringMethods(unittest.TestCase):

    def test_choose_race(self):
        player1 = Player('Human','p1')
        player1.choose_race()
        print(player1.my_race,Humans(),player1.my_race.unit_class_list)







if __name__ == '__main__':
    unittest.main()