from library import utility

class Player:
    def __init__(self, race, player_name):
        self.race = race
        self.player_name = player_name
        self.my_race = None
        self.unit_list = []
        self.choose_race()

    def choose_race(self):
        if self.race == 'Humans':
            from Race_tech_tree import Humans
            self.my_race = Humans()
            for unit_and_buildings in self.my_race.start_unit_list:
                self.create_unit(unit_and_buildings)
        elif self.race == 'Orcs':
            from Race_tech_tree import Orcs
            self.my_race = Orcs()

    def create_unit(self, unit_class):
        my_unit = unit_class()
        my_unit.owner = self.player_name
        self.unit_list.append(my_unit.name)

    def check_a_building(self,building,unit_class):
        pass
    #     to dogit


    def whether_unit_alive(self):
        for unit in self.unit_list:
            if unit.current_hp == 0:
                self.unit_list.remove(unit)

