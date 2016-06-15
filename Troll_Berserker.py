from Unit import Unit

class Troll_berserker(Unit):
    def __init__(self):
        Unit.__init__(self,450,25,'pierce','medium',0,1,2.31,)
        self.do_berserk = False
        self.berserk_cooldown = 30
        self.berserk_cooldown_remaining = 0

    def berserk(self):
        if self.berserk_cooldown_remaining == 0:
            self.launch_berserk()
            self.do_berserk = True

    def launch_berserk(self):
        self.attack *= 2

    def underattacked(self, damage, underattack_type):
        if self.do_berserk:
            damage = damage * 2
        Unit.underattacked(self, damage, underattack_type)

    def cancel_berserk(self):
        self.attack *= 0.5
        self.do_berserk = False

    def berserk_reduce_cooldown(self, fps):
        self.berserk_cooldown_remaining -= 1 / fps
        if self.berserk_cooldown_remaining - 12 < 0.001 \
                and 0 < self.berserk_cooldown_remaining - 12:
            self.cancel_berserk()
        elif self.berserk_cooldown_remaining < 0.001:
            self.berserk_cooldown_remaining = 0

    def can_reduce_heal_cooldown(self):
        if self.berserk_cooldown_remaining > 0:
            return True

    def spell_clock(self,fps):
        if self.can_reduce_heal_cooldown():
            self.berserk_reduce_cooldown(fps)