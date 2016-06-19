from Unit import Unit
from Attack import Attack

class Flying_Machine(Unit):
    def __init__(self):
        Unit.__init__(self,200,7.5,'siege','heavy',2,1,2.5,0,0,
                      'air',['air'])
        self.air_attack = 14.5
        self.air_attack_cooldown = 2
        self.air_attack_type = 'pierce'

    def force_attack(self, enemy):
        if enemy.position == 'air':
            getAttack = Attack(self.air_attack, self.air_attack_type, self.name)
            getAttack.sendAttack(enemy)
        else:
            Unit.force_attack(self, enemy)

    def launch_attack(self, enemy):
        """

        :param enemy: Unit
        :return: function
        """
        if enemy.position in self.attackable_position:
            if self.cooldown_remaining == 0:
                self.force_attack(enemy)
                if enemy.position == 'air':
                    self.cooldown_remaining = self.air_attack_cooldown
                else:
                    self.cooldown_remaining = self.cooldown
        else:
            print('You cannot attack')

    def flying_machine_bombs(self):
        self.attackable_position.append('ground')

