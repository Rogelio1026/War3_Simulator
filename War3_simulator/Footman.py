from Unit import Unit
from Attack import NormalAttack

class Footman(Unit,NormalAttack):
    def __init__(self):
        NormalAttack.__init__(self)
        Unit.__init__(self, 420, 12.5)

    def defend(self):
        pass
