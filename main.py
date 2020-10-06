import time
import random

from fruit import Fruit
from basket import Basket
from power import Power
from poison import Poison

basket = Basket("marcos","green",0,0,3)

def add_style(func):
    def wrapper():
        str = func()
        return f"**** {str} ****"
    return wrapper

def start_game(timer):

    mango = Fruit("mango", 15, "mango.png", .2)
    forbiddenMango = Fruit("forbidden mango", -15, "mango.png", .7)
    apple = Fruit("apple",10,"apple.png",.5)
    badApple = Fruit("bad apple",-10,"badapple.png",.5)
    orange = Fruit("orange", 5, "orange.png", .7)
    pineapple = Fruit("pinapple", 15, "pinapple.png", .4)
    fruits = [mango, forbiddenMango, apple, badApple, orange, pineapple]

    power = Power("Faster Basket","Faster Basket",0,"power1.png",.9,5)
    power2 = Power("10 Extra Points", "10 Extra Points", 10,"power2.png", .9,0)

    powers = [power, power2]
    poisons = [Poison.send_poison(), Poison.slower(), Poison.burn()]

    seconds = timer
    start = time.time()
    time.process_time()
    elapsed = 0
    power_random = random.randint(0,seconds)

    print("Get Ready!")
    print(f"You have {seconds} seconds to catch as many fruits as you can!")
    while elapsed <= seconds:
        print(f"Total score: {basket.get_score()}")
        elapsed = time.time() - start
        fruit = random.choice(fruits)
        pw = random.choice(powers)
        poison = random.choice(poisons)
        slowed, poison_score, message = poison
        basket.catch_fruit(fruit.get_score())
        if int(elapsed) == power_random:
            basket.catch_fruit(pw.get_score())
            style = add_style(pw.announce)
            print(style())
            basket.use_power(pw.get_time(), pw.get_ability(), pw.get_score())
        if int(elapsed) == 3:
            print(message)
            basket.catch_fruit(poison_score)
            basket.set_speed(slowed)

        print(f"Catched: {fruit.get_name()}")    
        time.sleep(1)
    
    basket.update_highsore()

    print(f"Game Over\nScore: {basket.get_score()} | Highscore: {basket.get_highscore()}")


start_game(30)


