import uuid
import time

armortype={'light':0,'medium':1,'heavy':2,'fortified':3,'hero':4,'unarmored':5}
normal_attack = (1, 1.5, 1, .7, 1, 1)
pierce_attack = (2, .75, 1, .35, .5, 1.5)
siege_attack = (1, .5, 1, 1.5, .5, 1.5)
magic_attack = (1.25, .75, 2, .35, .5, 1)
chaos_attack = (1, 1, 1, 1, 1, 1)
spell_attack = (1, 1, 1, 1, .7, 1)
hero_attack = (1, 1, 1, .5, 1, 1)
attack_type = {'normal': normal_attack, 'pierce': pierce_attack, 'siege': siege_attack, 'magic': magic_attack, 'chaos':
    chaos_attack, 'spell': spell_attack, 'hero': hero_attack}
class Unit:
    def __init__(self, max_hp=1, attack=0, armor_type='unarmored', armor=0, hp_regeneration_rate=1, hp_regenerate=True):
        self.name = uuid.uuid4()
        self.max_hp = max_hp
        self.attack = attack
        self.armor_type = armor_type
        self.armor = armor
        self.current_hp = max_hp
        self.hp_regeneration_rate = hp_regeneration_rate
        self.hp_regenerate = hp_regenerate

    def underattacked(self,damage,underattack_type):
        self.damage = damage
        self.underattack_type = attack_type[underattack_type]
        self.damage_change = self.underattack_type[armortype[self.armor_type]]
        if self.armor >= 0:
            self.damage_change = self.damage_change * (1 - self.armor * 0.06 / (1 + self.armor * 0.06))
        else:
            self.damage_change = self.damage_change * (2 - 0.94^self.armor)
        self.current_hp = self.current_hp - self.damage * self.damage_change
        if self.current_hp < 0:
            self.current_hp = 0
        # if self.hp_regenerate:
        #     while self.current_hp < self.max_hp:
        #         time.sleep(1)
        #         self.current_hp = self.current_hp + self.hp_regenration_rate
        #         if self.current_hp > self.max_hp:
        #             self.current_hp = self.max_hp
    def alive(self):
        return self.current_hp > 0

