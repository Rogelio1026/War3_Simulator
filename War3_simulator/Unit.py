import uuid
class Unit:
    def __init__(self, max_hp, attack):
        self.name = uuid.uuid4()
        self.max_hp = max_hp
        self.damage = attack
        self.current_hp = max_hp

    def underattacked(self, damage):
        self.current_hp = self.current_hp - damage
        if self.current_hp < 0:
            self.current_hp = 0

    def alive(self):
        return self.current_hp > 0


class PierceAttack:
    def __init__(self):
        self.attack_type = "pierce attack"

class NormalAttack:
    def __init__(self):
        self.attack_type = "normal attack"

class Peasant(Unit,NormalAttack):
    def __init__(self):
        NormalAttack.__init__(self)
        Unit.__init__(self, 220, 10)

class Peon(Unit,NormalAttack):
    def __init__(self):
        NormalAttack.__init__(self)
        Unit.__init__(self, 250, 10)

class Rifleman(Unit,PierceAttack):
    def __init__(self):
        PierceAttack.__init__(self)
        Unit.__init__(self, 560, 20)

if __name__ == '__main__':
    peasant = Peasant()
    peon = Peon()
    rifleman = Rifleman()
    print(peasant.max_hp,peon.max_hp,rifleman.max_hp)
    print(peasant.attack_type,peon.attack_type,rifleman.attack_type)
    print(peasant.damage,peon.damage,rifleman.damage)
    peasant.underattacked(100)
    print(peasant.current_hp,peasant.alive())
    peasant.underattacked(150)
    print(peasant.current_hp,peasant.alive())




