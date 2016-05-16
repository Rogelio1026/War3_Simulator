from Unit import Unit
class Building(Unit):
    def __del__(self):
        Unit.__init__(self, can_move=False)
