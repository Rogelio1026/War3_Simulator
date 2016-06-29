

class Player:
    def __init__(self, race, player_name):
        self.race = race
        self.player_name = player_name
        self.my_race = None
        self.unit_list = []

    def choose_race(self):
        if self.race == 'Human':
            from Race_tech_tree import Humans
            self.my_race = Humans()
        elif self.race == 'Orcs':
            from Race_tech_tree import Orcs
            self.my_race = Orcs()

    def create_unit(self,unit_class):
        if unit_class in self.my_race.unit_class_list and self.race.check_unit_availablity(unit_class) == True:
            my_unit = unit_class()
            self.unit_list.append(my_unit.name)

    def whether_unit_alive(self):
        for unit in self.unit_list:
            if unit.current_hp == 0:
                self.unit_list.remove(unit)

