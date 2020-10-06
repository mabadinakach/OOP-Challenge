import time

class Basket:
    def __init__(self, name ,color, x, score, speed, highscore = 0):
        self.name = name
        self._color = color
        self._x = x
        self._score = score
        self.speed = speed
        self._highscore = highscore
    
    def get_score(self):
        return self._score

    def get_highscore(self):
        return self._highscore

    def set_speed(self, speed):
        self.speed += speed

    def update_highsore(self):
        if self._score > self._highscore:
            self._highscore = self._score

    def use_power(self, seconds, ability, _score):
        start = time.time()
        time.process_time()   
        elapsed = 0
        self.speed += _score
        while elapsed <= seconds:
            elapsed = time.time() - start
            if seconds > 0:
                print(f"{int(seconds)-int(elapsed)} seconds remaining")
            time.sleep(1)
        self.speed -= _score
        

    def catch_fruit(self, points):
        self._score += points

    