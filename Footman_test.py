import unittest
from Footman import Footman

class TestStringMethods(unittest.TestCase):
    def test_damage_change_lookup(self):
        footman = Footman()
        damage_change = footman.damage_change_lookup('pierce', 'heavy')
        self.assertEqual(damage_change, 1)
        footman.defend()
        damage_change = footman.damage_change_lookup('pierce', 'heavy')
        self.assertEqual(damage_change, .5)
        footman.cancelDefend()
        damage_change = footman.damage_change_lookup('pierce', 'heavy')
        self.assertEqual(damage_change, 1)

if __name__ == '__main__':
    unittest.main()