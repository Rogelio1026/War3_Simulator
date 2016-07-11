from Unit import Unit
class Blacksmith(Unit):
    def __init__(self):
        Unit.__init__(self,1200,0,'normal','fortified',5,0,0,0,0,'building',[])
        self.unit_availbality = {}
        self.last_name = 'blacksmith'
        self.name = self.last_name + self.name
        self.iron_forged_swords = False

    def upgrade_iron_forged_swords(self):
        self.owner.whether_iron_forged_swords = True

    def upgrade_steel_forged_swords(self):
        if self.owner.whether_iron_forged_swords == True:
            self.owner.whether_steel_forged_swords = True

    def upgrade_mithril_forged_swords(self):
        if self.owner.whether_steel_forged_swords == True:
            self.owner.whether_mithril_forged_swords = True