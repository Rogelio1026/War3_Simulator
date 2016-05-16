import unittest
from War3_simulator import Humans_Peasant
class TestStringMethods(unittest.TestCase):

    def test_creat_Humans_Peasant(self):
        Peasant=Humans_Peasant(10)
        Peasant.creat_Humans_Peasant(1)
        self.assertEqual(Peasant.max_hp, 220)
        self.assertEqual(Peasant.armor, 0)

if __name__ == '__main__':
    unittest.main()