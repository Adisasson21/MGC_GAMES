from time import sleep
import time
"from Score import add_score"


def welcome():
    counter = 0
    limit_counter = 3
    while counter < limit_counter:
        counter += 1
        name = str(input("What is yors name? "))
        if name.isalpha():
            print(f'Hello {name} and welcome to the World of Gmaes(WoG).\nHere you can find many cool games to play.')
            return
        else:
            print("Somethimg wrong, Try again.")
    else:
        print("You've tried enough")


def level_difficult():
    Difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    try:
        if Difficulty == 1 or 2 or 3 or 4 or 5:
            print(f'You have chose game difficulty - {Difficulty}')
            return Difficulty
        else:
            print("You wrote something wrong")
    except ValueError:
        print("You have not write a number")

        
def load_game():
    print("""
            Please choose a game to play:
            1: Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS}
            """)
    The_number = input("Write down the number of the selected game (1 / 2 / 3): ")
    if The_number == "1":
        print("""You chose --- Memory Game - a sequence of numbers will appear for 1 second and you have to
            guess it back""")
        time.sleep(1)
        return The_number
    elif The_number == "2":
        print("""You chose --- Guess Game - guess a number and see if you chose like the computer""")
        time.sleep(1)
        return The_number
    elif The_number == "3":
        print("""You chose --- Currency Roulette - try and guess the value of a random amount of USD in ILS""")
        time.sleep(1)
        return The_number
    elif The_number.isdigit() or not "1" and not "2" and not "3":
        print("Sorry, the number that you chose is invalid.")
    else:
        print("You don't write a number.")
    
    

