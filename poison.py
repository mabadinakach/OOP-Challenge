class Poison:
    @staticmethod
    def send_poison():
        message = "You have been poisoned -4 points"
        slowed = 0
        score = -4
        return slowed, score, message

    @staticmethod
    def slower():
        message = "Ups you have been slowed, haha"
        slowed = -5
        score = 0
        return slowed, score, message

    @staticmethod
    def burn():
        message = "You are burning..."
        slowed = -5
        score = -10
        return slowed, score, message