class Fruit:
    def __init__(self, name, score, img, falling_speed):
        self.name = name
        self.score = score
        self.img = img
        self.falling_speed = falling_speed

    def get_score(self):
        return self.score
    
    def get_falling_speed(self):
        return self.falling_speed

    def get_name(self):
        return self.name

    