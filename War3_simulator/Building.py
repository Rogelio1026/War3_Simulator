from Unit import Unit
class Building(Unit):
    def __init__(self):
        Unit.__init__(self, 1500, 0, 'fortified', 0, False)

    def build(self):
        pass
