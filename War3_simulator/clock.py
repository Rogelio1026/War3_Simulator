from Humans_peasant import Peasant

class Clock:
    def __init__(self,fps,):
        self.fps = fps
        self.recipients = []

    def tick(self):
        for recipient in self.recipients:
            recipient.tick()

    def add_recipients(self,recipient):
        self.recipients.append(recipient)

if __name__ == '__main__':
    game = Clock(24)
    peasant = Peasant()
    game.add_recipients(peasant)
    game.tick()