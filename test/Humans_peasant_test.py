import unittest
from Humans_peasant import Peasant
class TestStringMethods(unittest.TestCase):

    def test_creat_Humans_Peasant(self):
        peasant=Peasant()
        self.assertEqual(peasant.armor_type, 'medium')
        self.assertEqual(peasant.armor, 0)
        peasant.militia()
        self.assertEqual(peasant.armor_type, 'heavy')
        self.assertEqual(peasant.armor, 4)
        peasant.back_to_work()
        self.assertEqual(peasant.armor_type, 'medium')
        self.assertEqual(peasant.armor, 0)
        self.assertEqual(peasant.whether_building, False)

if __name__ == '__main__':
    unittest.main()