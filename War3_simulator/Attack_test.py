from Humans_peasant import Peasant
import unittest
class TestStringMethods(unittest.TestCase):
    def test_under_attecked(self):
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

if __name__ == '__main__':
    unittest.main()