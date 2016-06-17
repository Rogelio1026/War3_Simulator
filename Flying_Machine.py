from Unit import Unit

class Flying_Machine(Unit):
    def __init__(self):
        Unit.__init__(self,200,14.5,'pierce','heavy',2,1,2,0,0,
                      'air',['air'])

