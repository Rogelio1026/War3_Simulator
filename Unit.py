Key = ['max_hp', 'armor', 'attack', 'armor_type', 'attack_type', 'can_move', 'speed',
       'can_attack', 'hp_regenration_rate', 'attack_range', 'food']

class Unit:
    def __init__(self, Key):
        self.Key = Key

    def under_attecked(self, damage):
        self.current_hp = self.current_hp - damage




