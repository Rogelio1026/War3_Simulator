from Priest import Priest
from Humans_peasant import Peasant
from Humans_Townhall import HumansTownhall
from Barracks import Barracks
from Troll_Berserker import Troll_berserker
from Orcs_peon import Peon
class Humans:
    def __init__(self):
        self.unit_class_list = ['Priest', 'Peasant']
        self.unit_availablity = ['Peasant']
        self.building_availablity = []
        self.upgrade_availablity = []
        self.start_unit_list = [Peasant,HumansTownhall]

    def initialized_units(self):
        for start_units in self.my_race.start_unit_list:
            self.create_unit(start_units)

    def check_tech_tree(self,unit_to_check):
        if unit_to_check in self.unit_availablity:
            return True





class Orcs:
    def __init__(self):
        self.unit_list = [Troll_berserker(), Peon()]