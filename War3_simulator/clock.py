class Game:
    def __init__(self,fps=24):
        self.fps = fps
        self.recipients = []

    def clock(self, t):
        """

        :param t: how many ticks
        :return:
        """
        for recipient in self.recipients:
            count = 0
            if recipient.alive:
                while count < t:
                    recipient.tick()
                    count += 1

    def add_recipients(self, recipient):
        self.recipients.append(recipient)


class Player:
    def __init__(self, race):
        self.race = race
        self.units = []

    def add_units(self,unit):
        self.units.append(unit)

    def clock(self, t):
        """

        :param t: int
        :return:
        """
        for unit in self.units:
            count = 0
            if unit.alive:
                while count < t:
                    unit.tick()
                    count += 1

if __name__ == '__main__':
    game = Game(20)
    print (game.fps)