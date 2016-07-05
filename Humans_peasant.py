from Unit import Unit
from Attack import NormalAttack

class Peasant(Unit,NormalAttack):
    def __init__(self):
        Unit.__init__(self, 220.0, 5.5, 'normal','medium', 0, 1.0)
        NormalAttack.__init__(self)
        self.name = 'peasant_'+self.name

    def militia(self):
        self.armor_type = 'heavy'
        self.armor = 4
        self.attack = 12.5
        self.cooldown = 1.2

    def back_to_work(self):
        self.armor_type = 'medium'
        self.armor = 0
        self.attack = 5.5
        self.cooldown = 2