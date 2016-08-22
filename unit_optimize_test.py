import uuid
from library import utility

class Unit:
    def __init__(self, general_stats=None, attack_stats=None, armor_stats=None, hp_mp_stats=None):
        if general_stats is None:
            general_stats = {"name": str(uuid.uuid4()),"last_name":'',"owner":'neutral',"position":'ground'}
        if attack_stats is None:
            attack_stats = {"attack":0,"attack_type":'normal',"attack_cooldown":2,"air_attack":0,
                            "air_attack_type":None,"air_attack_cooldown":2,"attackable_position":['ground','building']}
        if armor_stats is None:
            armor_stats = {"armor":0,"armor_type":'unarmored'}
        if hp_mp_stats is None:
            hp_mp_stats = {"max_hp":1,"hp_regeneration":1,"mana":0,"mana_regeneration":0}
        self.name = general_stats["name"]
        self.last_name = general_stats["last_name"]
        self.max_hp = hp_mp_stats["max_hp"]
        self.attack = attack_stats["attack"]
        self.attack_type = attack_stats["attack_type"]
        self.armor_type = armor_stats["armor_type"]
        self.armor = armor_stats["armor"]
        self.current_hp = hp_mp_stats["max_hp"]
        self.hp_regeneration_rate = hp_mp_stats["hp_regeneration_rate"]
        self.cooldown = attack_stats["attack_cooldown"]
        self.cooldown_remaining = 0
        self.max_mana = hp_mp_stats["max_mana"]
        self.current_mana = hp_mp_stats["max_mana"]
        self.mana_regeneration_rate = hp_mp_stats["max_mana_regeneration_rate"]
        self.position = general_stats["position"]
        self.attackable_position = attack_stats["attackable_position"]
        self.air_attack = 0
        self.air_attack_cooldown = 0
        self.air_attack_type = None
        self.time_ralated_functions = [self.hp_regenerate, self.mana_regenerate, self.reduce_cooldown]
        self.owner = general_stats["owner"]
        self.stats_upgrade_list = {}



class Sub_unit(Unit):
    def __init__(self):
        Unit.__init__(self,general_stats={"name": str(uuid.uuid4()),"last_name":'456'})

if __name__ == '__main__':
    unit = Unit()
    print(unit.name)
    subunit = Sub_unit()
    print(subunit.name)

