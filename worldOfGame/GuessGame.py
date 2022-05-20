from random import randint


def generate_number(level):
    secret_number = randint(1, level)
    return secret_number


def get_guess_from_user(level):
    guess = int(input(f"Guess number between 1 - {level}"))
    return guess


def compare_results(level):
    secret = generate_number(level)
    guess = get_guess_from_user(level)
    if secret == guess:
        return True
    else:
        return False


def play(level):
    res = compare_results(level)
    if res:
        print("Great !!!  yow won the game")
    else:
        print("Try next time!")


