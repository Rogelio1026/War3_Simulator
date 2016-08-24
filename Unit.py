import uuid
from Attack import Attack
from library import utility

armortype = {'light': 0, 'medium': 1, 'heavy': 2, 'fortified': 3, 'hero': 4, 'unarmored': 5}
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
    # def __init__(self, max_hp=1, attack=0, attack_type='normal', armor_type='unarmored', armor=0,
    #              hp_regeneration_rate=1, cooldown=2, max_mana=0, mana_regeneration_rate=0, position='ground',
    #              attackable_position=['ground', 'building'], owner='neutral', whether_building=False,
    #              attack_stats=None):
    #     if attack_stats is None:
    #         attack_stats = {"groud_attack": 1}
    #     self.name = str(uuid.uuid4())
    #     self.last_name = ''
    #     self.max_hp = max_hp
    #     self.attack = attack
    #     self.attack_type = attack_type
    #     self.armor_type = armor_type
    #     self.armor = armor
    #     self.current_hp = max_hp
    #     self.hp_regeneration_rate = hp_regeneration_rate
    #     self.cooldown = cooldown
    #     self.cooldown_remaining = 0
    #     self.max_mana = max_mana
    #     self.current_mana = max_mana
    #     self.mana_regeneration_rate = mana_regeneration_rate
    #     self.position = position
    #     self.attackable_position = attackable_position
    #     self.air_attack = 0
    #     self.air_attack_cooldown = 0
    #     self.air_attack_type = None
    #     self.time_ralated_functions = [self.hp_regenerate, self.mana_regenerate, self.reduce_cooldown]
    #     self.owner = owner
    #     self.whether_building = whether_building
    #     self.stats_upgrade_list = {}
    def __init__(self, general_stats=None, attack_stats=None, armor_stats=None, hp_mp_stats=None):
        if general_stats is None:
            general_stats = {"name": str(uuid.uuid4()),"last_name":'',"owner":'neutral'}
        if attack_stats is None:
            attack_stats = {"attack":0,"attack_type":'normal',"attack_cooldown":2,"air_attack":0,
                            "air_attack_type":None,"air_attack_cooldown":2,"attackable_position":['ground','building']}
        if armor_stats is None:
            armor_stats = {"armor":0,"armor_type":'unarmored',"position":'ground'}
        if hp_mp_stats is None:
            hp_mp_stats = {"max_hp":1,"hp_regeneration_rate":1,"max_mana":0,"mana_regeneration_rate":0}
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
        self.mana_regeneration_rate = hp_mp_stats["mana_regeneration_rate"]
        self.position = armor_stats["position"]
        self.attackable_position = attack_stats["attackable_position"]
        self.air_attack = 0
        self.air_attack_cooldown = 0
        self.air_attack_type = None
        self.time_ralated_functions = [self.hp_regenerate, self.mana_regenerate, self.reduce_cooldown]
        self.owner = general_stats["owner"]
        self.stats_upgrade_list = {}

    def tick(self, fps):
        """
        This function is called whenever time changed
        :return: function
        """
        for functions in self.time_ralated_functions:
            functions(fps)

    def spell_clock(self, fps):
        pass

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

    def underattacked(self, damage, underattack_type):
        """

        :param damage: is double
        :param underattack_type: is str
        :return:current hp
        """
        damage_change = Unit.damage_change_lookup(self, underattack_type, self.armor_type)
        damage_soak = Unit.damage_soak(self.armor)
        self.current_hp = self.current_hp - damage * damage_change * damage_soak
        if self.current_hp <= 0:
            self.current_hp = 0
            Unit.alive(self)

    def force_attack(self, enemy):
        if enemy.position == 'air':
            getAttack = Attack(self.air_attack, self.air_attack_type, self.name)
            getAttack.sendAttack(enemy)
        else:
            getAttack = Attack(self.attack, self.attack_type, self.name)
            getAttack.sendAttack(enemy)

    def damage_change_lookup(self, underattack_type, armor_type):
        """
        :param underattakc_type: is str
        :param armor_type: is str
        :return: damage change
        """
        underattack_type = attack_type[underattack_type]
        damage_change = underattack_type[armortype[armor_type]]
        return damage_change

    @staticmethod
    def damage_soak(armor):
        """
        define influence of positive or negative armor type
        :param armor: is int
        :return: double = damage change
        """
        if armor >= 0:
            return 1 - armor * 0.06 / (1 + armor * 0.06)
        else:
            return 2 - 0.94 ** armor

    def can_regenerate_hp(self):
        return 0 < self.current_hp and self.current_hp < self.max_hp

    def hp_regenerate(self, fps):
        """

        :return:current_hp
        """
        if self.can_regenerate_hp():
            self.current_hp += self.hp_regeneration_rate / fps
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp

    def can_regenerate_mana(self):
        return 0 < self.max_mana and self.current_mana < self.max_mana

    def mana_regenerate(self, fps):
        if self.can_regenerate_mana():
            self.current_mana += self.mana_regeneration_rate / fps
            if self.current_mana > self.max_mana:
                self.current_mana = self.max_mana

    def alive(self):
        return self.current_hp > 0

    def reduce_cooldown(self, fps):
        self.cooldown_remaining = utility.cooldown(self.cooldown_remaining, fps)

    def receive_upgrade(self, tech_to_upgrade):
        if tech_to_upgrade in self.stats_upgrade_list:
            self.stats_upgrade_list[tech_to_upgrade]
