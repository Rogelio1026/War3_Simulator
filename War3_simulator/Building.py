from Unit import Unit
class Building(Unit):
    def __init__(self):
        Unit.__init__(self, hp_regenerate_rate=0, hp_regenerate=False)

    def build(self):
        pass
