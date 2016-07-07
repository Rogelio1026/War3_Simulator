from Unit import Unit

class Knight(Unit):
    def __init__(self):
        Unit.__init__(self, 835,34,'normal','heavy',5,1,1.4,0,0,'ground',['ground','building'])
        self.last_name = 'knight'
        self.name = self.last_name + self.name