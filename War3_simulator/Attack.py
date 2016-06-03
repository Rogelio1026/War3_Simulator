class PierceAttack:
    def __init__(self):
        self.attack_type = "pierce"

class NormalAttack:
    def __init__(self):
        self.attack_type = "normal"

class Attack:
    def __init__(self, damage, attack_type, attacker):
        self.damage = damage
        self.attack_type = attack_type
        self.attacker = attacker

    def sendAttack(self, enemies):
        for enemy in enemies:
            enemy.underattacked(self.damage, self.attack_type)

