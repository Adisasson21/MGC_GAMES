from Live import welcome, load_game
from CurrencyRouletteGame import play3
from MEMORYGAME import play1
from GuessGame import play2


welcome()
load_game()
the_number_result = load_game


if the_number_result == 1:
    play1()
elif the_number_result == 2:
    play2()
elif the_number_result == 3:
    play3()
