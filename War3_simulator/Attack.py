class damage:
    def __init__(self, attack_type, armor_type, attacker, defender):
        self.attack_type = attack_type
        self.armor_type = armor_type
        self.attacker = attacker
        self.defender = defender

class PierceAttack:
    def __init__(self):
        self.attack_type = "pierce attack"

class NormalAttack:
    def __init__(self):
        self.attack_type = "normal attack"