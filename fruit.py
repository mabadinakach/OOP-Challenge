class Fruit:
    def __init__(self, name, score, img, falling_speed):
        self._name = name
        self._score = score
        self._img = img
        self._falling_speed = falling_speed

    def announce(self):
        return self._name

    def get_score(self):
        return self._score
    
    def get_falling_speed(self):
        return self._falling_speed

    def get_name(self):
        return self._name

    