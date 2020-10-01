from fruit import Fruit

class Power(Fruit):
    def __init__(self, ability, name, score, img, falling_speed, time):
        super().__init__(name, score, img, falling_speed)
        self.ability = ability
        self.time = time

    def announce(self):
        return f"{self.ability}"
    
    def get_ability(self):
        return f'Using {self.ability}'

    def get_time(self):
        return int(self.time)
