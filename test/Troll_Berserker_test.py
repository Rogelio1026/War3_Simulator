import  unittest
from Troll_Berserker import Troll_berserker
from Humans_peasant import Peasant
from clock import Game
class TestStringMethods(unittest.TestCase):

    def test_berserk(self):
        game = Game()
        troll_berserker = Troll_berserker()
        peasant = Peasant()
        game.add_recipients(troll_berserker)
        self.assertEqual(troll_berserker.berserk_cooldown_remaining,0)
        peasant.current_hp = 200
        troll_berserker.force_attack(peasant)
        self.assertEqual(peasant.current_hp,181.25)
        troll_berserker.cooldown_remaining = 0
        troll_berserker.berserk()
        peasant.current_hp = 200
        troll_berserker.force_attack(peasant)
        self.assertEqual(peasant.current_hp, 162.5)

if __name__ == '__main__':
    unittest.main()