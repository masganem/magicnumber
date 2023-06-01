import random

class GuessNumberGame:
    def __init__(self, target_number, max_attempts=5):
        self.target_number = target_number
        self.max_attempts = max_attempts
        self.current_attempt = 0

    def guess(self, number):
        self.current_attempt += 1
        if self.current_attempt > self.max_attempts:
            return "No attempts left"
        if number == self.target_number:
            return "Correct guess"
        else:
            return "Incorrect guess"

def game():
    target = random.randint(1, 10)
    game = GuessNumberGame(target)
    for _ in range(5):
        number = int(input("Guess a number from 1 to 10: "))
        print(game.guess(number))

if __name__ == "__main__":
    game()
