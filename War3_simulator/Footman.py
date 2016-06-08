from Unit import Unit
from Attack import NormalAttack

normal_attack = (1, 1.5, 1, .7, 1, 1)
pierce_attack = (2, .75, 1, .35, .5, 1.5)
siege_attack = (1, .5, 1, 1.5, .5, 1.5)
magic_attack = (1.25, .75, 2, .35, .5, 1)
chaos_attack = (1, 1, 1, 1, 1, 1)
spell_attack = (1, 1, 1, 1, .7, 1)
hero_attack = (1, 1, 1, .5, 1, 1)
attack_type = {'normal': normal_attack, 'pierce': pierce_attack, 'siege': siege_attack, 'magic': magic_attack, 'chaos':
    chaos_attack, 'spell': spell_attack, 'hero': hero_attack}


class Footman(Unit,NormalAttack):
    def __init__(self):
        NormalAttack.__init__(self)
        Unit.__init__(self, 420, 12.5, armor_type='heavy', armor=2,
                      hp_regeneration_rate=1, cooldown=1.35)
        self.defence = False

    def defend(self):
        self.defence = True

    def cancelDefend(self):
        self.defence = False

    def damage_change_lookup(self, underattack_type, armor_type):
        """
        :param underattakc_type: is str
        :param armor_type: is str
        :return: damage change
        """
        if underattack_type == 'pierce' and self.defence:
            return .5
        underattack_type = attack_type[underattack_type]
        damage_change = underattack_type[2]
        return damage_change

