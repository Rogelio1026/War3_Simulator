import unittest
from Priest import Priest
from Humans_peasant import Peasant
from clock import Game
class TestStringMethods(unittest.TestCase):

    def test_heal(self):
        priest = Priest()
        peasant = Peasant()
        peasant.current_hp = 150
        self.assertEqual(peasant.current_hp, 150)
        priest.heal(peasant)
        self.assertEqual(peasant.current_hp, 175)
        self.assertEqual(priest.current_mana,195)

    def test_heal_reduce_cooldown(self):
        game = Game()
        priest = Priest()
        peasant = Peasant()
        game.add_recipients(priest)
        self.assertEqual(priest.heal_cooldown_remaining, 0)
        priest.heal(peasant)
        self.assertEqual(priest.heal_cooldown_remaining, 1)
        count = 0
        t = 24
        while count < t:
            game.clock()
            count += 1
        self.assertEqual(priest.heal_cooldown_remaining, 0)
        priest.heal(peasant)
        count = 0
        t = 12
        while count < t:
            game.clock()
            count += 1
        print(priest.heal_cooldown_remaining)
        peasant.current_hp = 150
        priest.heal(peasant)
        self.assertEqual(peasant.current_hp, 150)

if __name__ == '__main__':
    unittest.main()