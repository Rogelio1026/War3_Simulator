from Unit import Unit

class Barracks(Unit):
    def __init__(self):
        Unit.__init__(self,1500,0,'normal','fortified',5,0,0,0,0,'building',None)
        self.unit_availbality_in_barracks = {'footman':[],'knight':['castle']}
        self.last_name = 'barracks'
        self.name = self.last_name+ self.name

    def check_tech_tree_in_barracks(self, Unit):
        """

        :param unit: the unit to build -instance
        :return: prerequisite -string
        """
        unit = Unit()
        unit_str = str(unit.last_name)
        return self.unit_availbality_in_barracks[unit_str]

    def creat_unit_in_barracks(self, Unit):
        a = self.check_tech_tree_in_barracks(Unit)
        if all(map(self.check_tech_tree_in_owner,a)):
            self.owner.create_unit(Unit)
        else:
            print('This tech is locked')

    def check_tech_tree_in_owner(self,tech):
        return tech in self.owner.tech_tree_list
