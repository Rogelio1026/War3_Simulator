from Unit import Unit
import uuid
class HumansPeasant(Unit):
    def __init__(self):
        Unit.__init__(self, hp=220, armor=0, some_random_uuid = uuid.uuid4())
