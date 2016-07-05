from Unit import Unit
from Humans_peasant import Peasant
class HumansTownhall(Unit):
    def __init__(self):
        Unit.__init__(self,1500,0,'normal','fortified',5,0,0,0,0,'building',None)
        self.unit_availbality_in_townhall = {'Peasant':True,'Barracks':True}

    def check_tech_tree_in_townhall(self,unit):
        return self.unit_availbality_in_townhall[unit]

    def creat_unit_in_townhall(self,unit):
        if self.check_tech_tree_in_townhall(unit):
            self.owner.create_unit(unit)



