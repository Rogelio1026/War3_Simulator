import uuid

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
    def __init__(self, max_hp=1, attack=0, armor_type='unarmored', armor=0, hp_regeneration_rate=1, hp_regenerate=True):
        self.name = uuid.uuid4()
        self.max_hp = max_hp
        self.attack = attack
        self.armor_type = armor_type
        self.armor = armor
        self.current_hp = max_hp
        self.hp_regeneration_rate = hp_regeneration_rate
        self.hp_regenerate = hp_regenerate

    def underattacked(self, damage, underattack_type):
        """

        :param damage: is double
        :param underattack_type: is str
        :return:current hp
        """
        damage_change = Unit.damage_change_lookup(underattack_type,self.armor_type)
        damage_soak = Unit.damage_soak(self.armor)
        self.current_hp = self.current_hp - damage * damage_change * damage_soak
        if self.current_hp < 0:
            self.current_hp = 0

    @staticmethod
    def damage_change_lookup(underattack_type, armor_type):
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

    def hpregenerate(self):
        if self.hp_regenerate:
            while self.current_hp < self.max_hp:
                self.current_hp = self.current_hp + self.hp_regenration_rate
                if self.current_hp > self.max_hp:
                    self.current_hp = self.max_hp

    def alive(self):
        return self.current_hp > 0

    def attack(self):
        """
        1.find enemy 2.get location 3.unit.move 4.enemy.underattack
        :return:
        """
        pass

    def tick(self, fps):
        """
        This function is called whenever time changed
        :return:
        """
        self.hpregenerate()