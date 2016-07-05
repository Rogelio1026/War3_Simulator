from Unit import Unit
from Humans_peasant import Peasant
class HumansTownhall(Unit):
    def __init__(self):
        Unit.__init__(self,1500,0,'normal','fortified',5,0,0,0,0,'building',None)
        self.unit_availbality_in_townhall = {'Humans_peasant.Peasant':[]}
        self.name = 'HumansTownhall_' + self.name

    def check_tech_tree_in_townhall(self,unit):
        """

        :param unit: the unit to build -instance
        :return: prerequisite -string
        """
        unit_str = str(unit)
        return self.unit_availbality_in_townhall[unit_str]

    def creat_unit_in_townhall(self,unit):
        a = self.check_tech_tree_in_townhall(unit)
        b = self.owner.unit_list
        if self.owner.unit_list == list(set(a).union(set(b))):
            self.owner.create_unit(unit)



