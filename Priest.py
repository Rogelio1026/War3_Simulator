from Unit import Unit
from library import utility

class Priest(Unit):
    def __init__(self):
        Unit.__init__(self, 290, 8.5, 'magic', max_mana=200,
                      mana_regeneration_rate=0.667)
        self.heal_cooldown = 1
        self.heal_cooldown_remaining = 0

    def heal(self,target):
        if self.heal_cooldown_remaining == 0 and target.alive():
            if self.current_mana >= 5:
                self.launch_heal(target)
            else:
                print('There is no mana')

    def launch_heal(self,target):
        target.current_hp += 25
        self.current_mana -= 5
        self.heal_cooldown_remaining = self.heal_cooldown
        if target.current_hp > target.max_hp:
            target.current_hp = target.max_hp

    def heal_reduce_cooldown(self,fps):
        self.heal_cooldown_remaining = utility.cooldown(self.heal_cooldown_remaining, fps)

    def can_reduce_heal_cooldown(self):
        if self.heal_cooldown_remaining > 0:
            return True

    def tick(self,fps):
        self.time_ralated_functions.append(self.heal_tick(fps))

    def heal_tick(self,fps):
        if self.can_reduce_heal_cooldown():
            self.heal_reduce_cooldown(fps)

    def dispel_magic(self,target):
        pass

