from MainScores import score_server
from live import load_game, welcome
import os

print(welcome("Guy"))
os.system("rm Scores.txt")
os.system("touch Scores.txt")


load_game()
score_server()


