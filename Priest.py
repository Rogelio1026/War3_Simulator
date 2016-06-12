from Unit import Unit

class Priest(Unit):
    def __init__(self):
        Unit.__init__(self, 290, 8.5, 'magic', max_mana=200,
                      mana_regeneration_rate=0.667)
        self.heal_cooldown = 1
        self.heal_cooldown_remaining = 0

    def heal(self,target):
        if self.heal_cooldown_remaining == 0 and target.alive():
            if self.current_mana >= 5:
                target.current_hp += 25
                self.current_mana -= 5
            else:
                print('There is no mana')




