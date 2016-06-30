from Unit import Unit

class Barracks(Unit):
    def __init__(self):
        # to do Unit.__init__(self,1500,0,'normal','fortified',5,0,0,0,0,'building',None)
        self.availbality_in_barracks = {'Footman':True}
