import unittest
from Humans_peasant import HumansPeasant
class TestStringMethods(unittest.TestCase):

    def test_creat_Humans_Peasant(self):
        Peasant=HumansPeasant()
        self.assertEqual(Peasant.max_hp, 220)
        self.assertEqual(Peasant.armor, 0)

if __name__ == '__main__':
    unittest.main()