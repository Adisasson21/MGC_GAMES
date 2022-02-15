import random
import time

from Live import level_difficult
from Score import add_score

difficulty = level_difficult()


def generate_number():
    secret_number = random.randrange(1, difficulty + 1)
    return secret_number


def get_guess_from_user():
    while True:
        try:
            guess = int(input(f'Your guess Is (you need to pick a number between 1-{difficulty}): '))
            if guess == 1 or 2 or 3 or 4 or 5:
                print(f'You guess {guess}')
                return guess
        except ValueError:
            print("you didnt write a number.")
        continue


def compare_results():
    Generate = generate_number()
    The_guess_number = get_guess_from_user()
    if The_guess_number == Generate:
        print("YOU WON")
        add_score(difficulty)
    else:
        print("SORRY, YOU LOST.")
  
def play2():
    compare_results()
    
    


