from Live import welcome
from Live import load_game
from Live import level_difficult
from Utils import Screen_cleaner
from os import system


def games():
    number = load_game()
    if number == "1":
        from MemoryGame import play1
        play1()
    elif number == "2":
        from GUESSGAME import play2
        play2()
    elif number == "3":
        from CurrencyRouletteGame import play3
        play3()
    else:
        print("you have write a anumber")
    """while True:
        Number_of_games = 0
        print("Do you want to play again? (yes or no) ")
        playagain = input().lower()
        while playagain == 'yes' or 'y':
            while Number_of_games < 3:
                games()
                Number_of_games += 1
        else:
            print(playagain)
            exit()"""




welcome()
games()




    



