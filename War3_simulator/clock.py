class Game:
    def __init__(self,fps=24.0):
        self.fps = fps
        self.recipients = []

    def clock(self):
        """

        :param t: how many ticks
        :return:
        """
        for recipient in self.recipients:
            if recipient.alive:
                recipient.tick(self.fps)


    def add_recipients(self, recipient):
        self.recipients.append(recipient)


class Player:
    def __init__(self, race):
        self.race = race
