from random import randint
from time import sleep


def generate_sequence(level):
    seq = []
    for i in range(0, level):
        seq.append(randint(1, 101))
    return seq


def get_list_from_user(level):
    print("enter the numbers that you saw (numer than click Enter and repet)")
    user_seq = []
    for i in range(level):
        print("-------------------")
        user_seq.append(int(input()))
    return user_seq


def is_list_equal(level):
    a = generate_sequence(level)
    print(a)
    sleep(0.7)
    for i in range(100):
        print()
    b = get_list_from_user(level)
    if sorted(a) == sorted(b):
        return True
    else:
        return False


def play(level):
    res = is_list_equal(level)
    if res:
        print("Great !!!  yow won the game")
        return True
    else:
        print("Try next time!")
        return False

