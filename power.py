from fruit import Fruit

class Power(Fruit):
    '''Class inherits from fruit and serves as a power-up fruit, it adds ability and time'''

    def __init__(self, ability, name, score, img, falling_speed, time):
        super().__init__(name, score, img, falling_speed)
        self._ability = ability
        self._time = time

    def announce(self):
        return f"POWER: {self._ability}"
    
    def get_ability(self):
        return f'Using {self._ability}'

    def get_time(self):
        return int(self._time)
