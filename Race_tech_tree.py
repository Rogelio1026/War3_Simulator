from Priest import Priest
from Humans_peasant import Peasant
from Troll_Berserker import Troll_berserker
from Orcs_peon import Peon
class Humans:
    def __init__(self):
        self.unit_class_list = [Priest(), Peasant()]


class Orcs:
    def __init__(self):
        self.unit_list = [Troll_berserker(), Peon()]