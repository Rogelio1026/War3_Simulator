from Unit import Unit
from Attack import NormalAttack

class Peon(Unit,NormalAttack):
    def __init__(self):
        NormalAttack.__init__(self)
        Unit.__init__(self, 250, 7.5, 'light')

