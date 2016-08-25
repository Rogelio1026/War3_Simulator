from Unit import Unit
from Attack import NormalAttack

class Peasant(Unit,NormalAttack):
    def __init__(self):
        Unit.__init__(self)
        attack_stats = {"attack": 0, "attack_type": 'normal', "attack_cooldown": 2, "air_attack": 0,
                        "air_attack_type": None, "air_attack_cooldown": 2,
                        "attackable_position": ['ground', 'building']}
        armor_stats = {"armor": 0, "armor_type": 'unarmored', "position": 'ground'}
        hp_mp_stats = {"max_hp": 1, "hp_regeneration_rate": 1, "max_mana": 0, "mana_regeneration_rate": 0}
        self.last_name = 'peasant'
        self.name = self.last_name + self.name

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