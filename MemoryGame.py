import collections
import random
from Live import level_difficult
import time
from os import system
from Score import add_score

difficulty = level_difficult()


def generate_sequence():
    list = []
    count_diffi = 0
    while count_diffi < difficulty:
        list.append(random.randrange(1, 101))
        count_diffi += 1
    print(list)
    time.sleep(3)
    """cls = lambda: system('cls')
    cls()"""
    return list


def get_list_from_user():
    guess_list = []
    count_guess = 0
    max = difficulty
    while count_guess < max:
        get_guess_from_user = int(input("GUESS NUMBER: "))
        guess_list.append(get_guess_from_user)
        count_guess += 1
    print(f"It's your guess numbers are, {guess_list}")
    time.sleep(1)
    return guess_list


def is_list_equal():
    The_List = generate_sequence()
    Guess_List = get_list_from_user()
    if collections.Counter(Guess_List) == collections.Counter(The_List):
        return True
    else:
        return False


def play1():
    list_equal = is_list_equal()
    if list_equal == True:
        print("YOU WON")
        add_score(difficulty)
    else:
        print("SORRY, YOU LOST.")

