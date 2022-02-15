import datetime
from Live import level_difficult
import random
from forex_python.converter import CurrencyRates
from Score import add_score


def get_money_interval():
    difficulty = level_difficult()
    date_obj = datetime.datetime(2020, 5, 23, 18, 36, 28, 151012)
    c = CurrencyRates()
    price_for = c.get_rates('USD', date_obj)

    amount_USD = int(random.randrange(1, 101))
    total_value_of_money = (amount_USD * price_for['ILS'])

    the_range = round(total_value_of_money, 1) - (5 - difficulty), round(total_value_of_money, 1) + (5 - difficulty)
    return the_range, amount_USD ,difficulty


def get_guess_from_user():
    The_range, x_dollars, score = get_money_interval()
    guess_currency = float(input(f'how much do you think $ {x_dollars} worth in ILS? '))
    if The_range[0] <= guess_currency <= The_range[1]:
        print("YOU WON")
        add_score(score)
    else:
        print("SORRY, YOU LOST.")

    
def play3():
    get_guess_from_user()


