from Unit import Unit
class Building(Unit):
    def __init__(self):
        Unit.__init__(self, attack=0, armor_type='fortified')

    def build(self):
        pass
