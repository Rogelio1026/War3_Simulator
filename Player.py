from library import utility
from Race_tech_tree import Humans
from Race_tech_tree import Orcs

class Player:
    def __init__(self, race, player_name):
        self.race = race
        self.player_name = player_name
        self.my_race = None
        self.unit_list = []
        self.tech_tree_list = []
        self.building_list = []
        self.choose_race()

    def choose_race(self):
        if self.race == 'Humans':
            self.my_race = Humans()
            for start_units in self.my_race.start_unit_list:
                self.create_unit(start_units)
        elif self.race == 'Orcs':
            self.my_race = Orcs()

    def create_unit(self, unit_class):
        my_unit = unit_class()
        my_unit.owner = self
        self.unit_list.append(my_unit.name)
        self.tech_tree_list.append(my_unit.last_name)

    def check_a_building(self,building,unit_class):
        pass



    def whether_unit_alive(self):
        for unit in self.unit_list:
            if unit.current_hp == 0:
                self.unit_list.remove(unit)

    def upgrade_buildings(self,building_before,building_after):
        """

        :param building_before: instance
        :param building_after:instance
        :return: upgrade unit_list & tech_tree_list
        """
        self.unit_list.append(building_after.name)
        self.unit_list.remove(building_before.name)
        self.tech_tree_list.append(building_after.last_name)
        self.tech_tree_list.remove(building_before.last_name)