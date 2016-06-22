from Unit import Unit
from Attack import Attack

class Flying_Machine(Unit):
    def __init__(self):
        Unit.__init__(self,200,7.5,'siege','heavy',2,1,2.5,0,0,
                      'air',['air'])
        self.air_attack = 14.5
        self.air_attack_cooldown = 2
        self.air_attack_type = 'pierce'


    def flying_machine_bombs(self):
        self.attackable_position.append('ground')

