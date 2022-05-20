from random import randint

import requests


def get_money_interval(level):
    url = 'https://v6.exchangerate-api.com/v6/c8af8a86c6d3aeaef7e72237/latest/USD'
    response = requests.get(url)
    data = response.json()
    cur = data["conversion_rates"]["ILS"]
    num = randint(1, 100)
    print(f"How much is {num}$ in ILS shekel")
    print(cur*num)
    res = [num*cur-(5-level), num*cur+(5-level)]
    return res


def get_guess_from_user():
    guess = float(input("enter your guess\n"))
    return guess


def play(level):
    cur = get_money_interval(level)
    guess = get_guess_from_user()
    if cur[0] <= guess <= cur[1]:
        print("Great !!!  yow won the game")
        return True
    else:
        print("Try next time!")
        return False



