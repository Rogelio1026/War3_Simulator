import unittest
from yuhaozheng import Unit
class TestStringMethods(unittest.TestCase):

    def test_under_attecked(self):
        footman=Unit(420)
        footman.under_attecked(100)
        self.assertEqual(footman.current_hp, 320)
        footman.under_attecked(100)
        self.assertEqual(footman.current_hp, 220)


if __name__ == '__main__':
    unittest.main()