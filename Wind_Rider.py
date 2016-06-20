from Unit import Unit
from Attack import Attack


class Wind_Rider(Unit):
    def __init__(self):
        Unit.__init__(self, 570, 40, 'pierce', 'light', 0, 1,2, 0,
                      0, 'air', ['ground','building','air'])
        self.air_attack = 40
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
