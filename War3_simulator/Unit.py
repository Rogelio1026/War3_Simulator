class Humans:
    def __init__(self, hp, armor, id):
        self.hp = hp
        self.armor = armor
        self.id = id
        self.current_hp = hp
    def under_attecked(self, damage):
        self.current_hp = self.current_hp - damage

class Humans_Peasant(Humans):
    def creat_Humans_Peasant(self, hp=220, armor=0, id=1):
        id=+1
        print('You creat a Humans Peasant')



