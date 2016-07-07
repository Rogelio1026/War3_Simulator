from Unit import Unit

class Footman(Unit):
    def __init__(self):
        Unit.__init__(self, 420, 12.5, armor_type='heavy', armor=2,
                      hp_regeneration_rate=1, cooldown=1.35)
        self.last_name = 'footman'
        self.name = self.last_name + self.name
        self._defence = False

    def defend(self):
        self._defence = True

    def cancelDefend(self):
        self._defence = False

    def underattacked(self, damage, underattack_type):
        if underattack_type == 'pierce' and self._defence:
            damage = damage * 0.5
        Unit.underattacked(self, damage, underattack_type)