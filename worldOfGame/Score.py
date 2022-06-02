import os

from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty*3) + 5
    try:
        if os.stat(SCORES_FILE_NAME).st_size > 0:
            my_file = open("Scores.txt", "r")
            for line in my_file.readlines():
                my_file = open("Scores.txt", "w")
                my_file.write(str(int(line)+POINTS_OF_WINNING)+"\n")
        else:
            my_file = open("Scores.txt", "w")
            my_file.write(str(POINTS_OF_WINNING))

    except OSError:
        print
        "No file"


