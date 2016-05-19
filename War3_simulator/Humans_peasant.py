from Unit import Unit
from Attack import NormalAttack

class Peasant(Unit,NormalAttack):
    def __init__(self):
        NormalAttack.__init__(self)
        Unit.__init__(self, 220, 10)