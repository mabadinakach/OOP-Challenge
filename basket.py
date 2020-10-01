import time

class Basket:
    def __init__(self, name ,color, x, score, speed, highscore = 0):
        self.name = name
        self._color = color
        self.x = x
        self.score = score
        self.speed = speed
        self.highscore = highscore
    
    def get_score(self):
        return self.score

    def get_highscore(self):
        return self.highscore

    def set_speed(self, speed):
        self.speed += speed

    def update_highsore(self):
        if self.score > self.highscore:
            self.highscore = self.score

    def use_power(self, seconds, ability, score):
        start = time.time()
        time.process_time()   
        elapsed = 0
        self.speed += score
        while elapsed <= seconds:
            elapsed = time.time() - start
            print(f"{int(seconds)-int(elapsed)} seconds remaining")
            time.sleep(1)
        self.speed -= score
        

    def catch_fruit(self, points):
        self.score += points

    