from Unit import Unit
from Attack import Attack


class Wind_Rider(Unit):
    def __init__(self):
        Unit.__init__(self, 570, 40, 'pierce', 'light', 0, 1,2, 0,
                      0, 'air', ['ground','building','air'])
        self.air_attack = 40
        self.air_attack_cooldown = 2
        self.air_attack_type = 'pierce'
