from Unit import Unit
class Building(Unit):
    def __init__(self):
        Unit.__init__(self, max_hp=1)

    def build(self):
        pass
