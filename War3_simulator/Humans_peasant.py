from Unit import Unit
class HumansPeasant(Unit):
    def __init__(self):
        Unit.__init__(self, hp=220, armor=0)

    def creat_Humans_Peasant(self,id):

        print('You creat a Humans Peasant')