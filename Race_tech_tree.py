from Priest import Priest
from Humans_peasant import Peasant
from Troll_Berserker import Troll_berserker
from Orcs_peon import Peon
class Humans:
    def __init__(self):
        self.unit_class_list = ['Priest', 'Peasant']
        self.unit_availablity = ['Peasant']
        self.building_availablity = []
        self.upgrade_availablity = []

    def check_unit_availablity(self,unit_to_check):
        if unit_to_check in self.unit_availablity:
            return True







class Orcs:
    def __init__(self):
        self.unit_list = [Troll_berserker(), Peon()]