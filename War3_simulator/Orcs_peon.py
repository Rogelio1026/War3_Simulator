from Unit import Unit
class OrcsPeon(Unit):
    def __init__(self):
        Unit.__init__(self, hp=250, armor=0)

    def creat_Orcs_Peon(self,id):

        print('You creat a Orcs Peon')