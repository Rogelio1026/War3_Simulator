class Unit:
    def __init__(self,max_hp):
        self.max_hp=max_hp
        self.current_hp=max_hp
    def under_attecked(self,damage):
        self.current_hp=self.current_hp-damage
