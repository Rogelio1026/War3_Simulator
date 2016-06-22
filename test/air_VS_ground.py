from Humans_peasant import Peasant
from Flying_Machine import Flying_Machine
from Wind_Rider import Wind_Rider
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
        flying_machine.flying_machine_bombs()
        flying_machine.launch_attack(peasant)
        self.assertEqual(compare_doubles(peasant.current_hp, 216.25),True)

    def test_air_vs_air(self):
        flying_machine = Flying_Machine()
        wind_rider = Wind_Rider()
        self.assertEqual(flying_machine.current_hp, 200)
        self.assertEqual(wind_rider.current_hp, 570)
        flying_machine.launch_attack(wind_rider)
        wind_rider.launch_attack(flying_machine)
        self.assertEqual(compare_doubles(flying_machine.current_hp, 164.286),True)
        self.assertEqual(wind_rider.current_hp, 541)

if __name__ == '__main__':
    unittest.main()