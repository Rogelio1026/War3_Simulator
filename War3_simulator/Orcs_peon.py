from Unit import Unit
import uuid
class OrcsPeon(Unit):
    def __init__(self):
        Unit.__init__(self, hp=250, armor=0, some_random_uuid = uuid.uuid4())
