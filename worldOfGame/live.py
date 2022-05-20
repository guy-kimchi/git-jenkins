
import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"


def load_game():
    flag = True
    showGames()
    while flag:
        while flag:
            try:
                game = int(input())
                if game < 1 or game > 4:
                    showGames()
                    continue
                break
            except ValueError:
                showGames()

        if game != 4:
            print("Please choose game difficulty from 1 to 5:")
            while flag:
                try:
                    level = int(input())
                    if level < 1 or level > 5:
                        print("Please choose game difficulty from 1 to 5:")
                        continue
                    break
                except ValueError:
                    print("Please choose game difficulty from 1 to 5:")

        if game == 1:
            MemoryGame.play(level)
            print("Press Enter to next round of game or 4 to Exit")
        elif game == 2:
            GuessGame.play(level)
            print("Press Enter to next round of game or 4 to Exit")
        elif game == 3:
            CurrencyRouletteGame.play(level)
            print("Press Enter to next round of game or 4 to Exit")
        elif game == 4:
            print("EXIT")
            break


def showGames():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print("4. Exit")





