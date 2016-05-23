armortype={'light':0,'medium':1,'heavy':2,'fortified':3,'hero':4,'unarmored':5}

class PierceAttack:
    def __init__(self):
        self.attack_type = "pierce attack"
        pierce_attack = [2, .75, 1, .35, .5, 1.5]
        self.damage_change = pierce_attack[armortype[self.armor_type]]

class NormalAttack:
    def __init__(self):
        self.attack_type = "normal attack"
        normal_attack = [1, 1.5, 1, .7, 1, 1]
        self.damage_change = normal_attack[armortype[self.armor_type]]
