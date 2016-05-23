import uuid
import time

class Unit:
    def __init__(self, max_hp, attack, armor_type, hp_regeneration_rate = 1, hp_regenerate = True):
        self.name = uuid.uuid4()
        self.max_hp = max_hp
        self.attack = attack
        self.armor_type = armor_type
        self.current_hp = max_hp
        self.hp_regeneration_rate = hp_regeneration_rate
        self.hp_regenerate = hp_regenerate

    def real_damage(self):
        pass

    def underattacked(self,damage,underattack_type):
        self.damage = damage
        self.underattack_type = underattack_type
        self.current_hp = self.current_hp - self.damage*self.damage_change
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

