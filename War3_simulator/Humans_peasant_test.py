import unittest
from Humans_peasant import Humans_Peasant
class TestStringMethods(unittest.TestCase):

    def test_creat_Humans_Peasant(self):
        Peasant=Humans_Peasant(1)
        Peasant.creat_Humans_Peasant()
        self.assertEqual(Peasant.max_hp, 220)
        self.assertEqual(Peasant.armor, 0)

if __name__ == '__main__':
    unittest.main()