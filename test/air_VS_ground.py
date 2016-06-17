from Humans_peasant import Peasant
from Flying_Machine import Flying_Machine
from clock import Game
from Unit import Unit
from library.test_utility import compare_doubles
import unittest

class TestStringMethods(unittest.TestCase):

    def test_ground_attack(self):
        peasant = Peasant()
        flying_machine = Flying_Machine()
        self.assertEqual(peasant.current_hp, 220)
        self.assertEqual(flying_machine.current_hp, 200)
        peasant.launch_attack(flying_machine)
        flying_machine.launch_attack(peasant)
        self.assertEqual(peasant.current_hp, 220)
        self.assertEqual(flying_machine.current_hp, 200)



if __name__ == '__main__':
    unittest.main()