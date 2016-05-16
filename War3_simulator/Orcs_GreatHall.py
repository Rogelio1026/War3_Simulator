from Building import Building
import uuid
class GreatHall(Building):
    def __init__(self):
        Building.__init__(self, hp=1500, armor=5, some_random_uuid = uuid.uuid4())