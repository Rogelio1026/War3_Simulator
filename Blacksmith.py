from Unit import Unit
class Blacksmith(Unit):
    def __init__(self):
        Unit.__init__(self,1200,0,'normal','fortified',5,0,0,0,0,'building',[])
        self.upgrades_availbality_in_blacksmith = {'melee_attack_l1':[],'melee_attack_l2':['keep'],
                                                   'melee_attack_l3': ['castle']}
        self.last_name = 'blacksmith'
        self.name = self.last_name + self.name
        self.iron_forged_swords = False

    def check_tech_tree_in_blacksmith(self,upgrades):
        """

        :param upgrades: upgrades to check -instance
        :return: prerequisite -string
        """
        return self.upgrades_availbality_in_blacksmith[upgrades]

    def upgrade_in_blacksmith(self,upgrades):
        upgrade_to_check = self.check_tech_tree_in_blacksmith(upgrades)
        if all(map(self.check_tech_tree_in_owner,upgrade_to_check)):
            self.owner.mark_upgrade_tech(upgrades)
            self.owner.upgrade_in_unit(upgrades)


    def check_tech_tree_in_owner(self,tech):
        return tech in self.owner.tech_tree_list
