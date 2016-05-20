from Humans_peasant import Peasant
import unittest
import time
class TestStringMethods(unittest.TestCase):
    def test_under_attacked(self):
        peasant = Peasant()
        self.assertEqual(peasant.max_hp,220)
        self.assertEqual(peasant.hp_regenerate,True)
        self.assertEqual(peasant.hp_regeneration_rate,1)
        peasant.underattacked(100)
        self.assertEqual(peasant.current_hp, 120)
        time.sleep(1)
        self.assertEqual(peasant.alive(), True)
        self.assertEqual(peasant.current_hp, 121)
        peasant.underattacked(150)
        self.assertEqual(peasant.current_hp, 0)
        self.assertEqual(peasant.alive(), False)

if __name__ == '__main__':
    unittest.main()