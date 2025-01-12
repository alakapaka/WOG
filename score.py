from io import open
from os import path

from utils import SCORES_FILE_NAME


def add_score(dif_lvl):
    game_score = dif_lvl * 3 + 5
    if path.exists(f'./{SCORES_FILE_NAME}'):
        file = open(f'./{SCORES_FILE_NAME}', 'r+')
        current_score = file.readline()
        new_score = int(current_score) + game_score
        print(f'''GOOD JOB! You scored: {game_score} points!
Your total score was: {current_score} points
and your new total score is: {new_score} points!!!''')
        file.truncate(0)
        file.seek(0)
        file.write(str(new_score))
    else:
        score_file = open(f'./{SCORES_FILE_NAME}', 'w')
        print(f'''GOOD JOB! You scored: {game_score} points!
        Your new total score is: {game_score} points!!!''')
        score_file.write(str(game_score))
