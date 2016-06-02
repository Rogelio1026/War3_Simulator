from Unit import Unit
from Attack import NormalAttack

class Peasant(Unit,NormalAttack):
    def __init__(self):
        Unit.__init__(self, 220.0, 5.5, 'normal','light', 0, 1.0)
        NormalAttack.__init__(self)
