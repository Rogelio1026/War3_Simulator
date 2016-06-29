from library import utility

class Player:
    def __init__(self, race, player_name):
        self.race = race
        self.player_name = player_name
        self.my_race = None
        self.unit_list = []
        self.choose_race()

    def choose_race(self):
        if self.race == 'Humans':
            from Race_tech_tree import Humans
            self.my_race = Humans()
        elif self.race == 'Orcs':
            from Race_tech_tree import Orcs
            self.my_race = Orcs()

    def create_unit(self,unit_class):
        print('%s' % unit_class,unit_class)
        if ('%s' % unit_class) in self.my_race.unit_class_list and self.my_race.check_unit_availablity('%s' % unit_class):
            my_unit = unit_class()
            print(my_unit.name)
            self.unit_list.append(my_unit.name)
        else:
            print('wrong')


    def whether_unit_alive(self):
        for unit in self.unit_list:
            if unit.current_hp == 0:
                self.unit_list.remove(unit)

