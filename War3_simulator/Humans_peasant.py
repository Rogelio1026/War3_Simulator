Key = ['max_hp', 'armor', 'attack', 'armor_type', 'attack_type', 'can_move', 'speed',
       'can_attack', 'hp_regenration_rate', 'attack_range', 'food']
class Unit:
    def __init__(self, Key):
        self.Key = Key

class Humans_Peasant(Unit):
    max_hp = 220
    armor = 0

    def __init__(self, id):
        self.id = id

    def creat_Humans_Peasant(self):
        print('You creat a Humans Peasant')