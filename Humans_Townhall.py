from Unit import Unit
from Humans_peasant import Peasant
class HumansTownhall(Unit):
    def __init__(self):
        Unit.__init__(self,1500,0,'normal','fortified',5,0,0,0,0,'building',None)
        self.unit_availbality_in_townhall = {'peasant':[]}
        self.last_name = 'HumansTownhall'
        self.name = self.last_name + self.name

    def check_tech_tree_in_townhall(self,Unit):
        """

        :param unit: the unit to build -instance
        :return: prerequisite -string
        """
        unit = Unit()
        unit_str = str(unit.last_name)
        return self.unit_availbality_in_townhall[unit_str]

    def creat_unit_in_townhall(self, Unit):
        unit_to_check = self.check_tech_tree_in_townhall(Unit)
        if all(map(self.check_tech_tree_in_owner,unit_to_check)):
            self.owner.create_unit(Unit)

    def check_tech_tree_in_owner(self,tech):
        return tech in self.owner.tech_tree_list

    def upgrade_to_keep(self):
        keep = Keep()
        keep.current_hp = keep.max_hp - self.max_hp + self.current_hp
        self.owner.upgrade_buildings(self,keep)

class Keep(HumansTownhall):
    def __init__(self):
        HumansTownhall.__init__(self)
        self.last_name = 'keep'
        self.name = self.last_name + self.name
        self.max_hp = 2000

    def upgrade_to_castle(self):
        castle = Castle()
        castle.current_hp = castle.max_hp - self.max_hp + self.current_hp
        self.owner.upgrade_buildings(self, castle)


class Castle(Keep):
    def __init__(self):
        Keep.__init__(self)
        self.last_name = 'castle'
        self.name = self.last_name + self.name
        self.max_hp = 2500