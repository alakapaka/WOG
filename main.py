from app import *


def welcome():
    username = get_str_user_decision('Please insert your name:', 1, True)
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    games = get_games()
    game_decision = get_int_user_decision(print_games(games), len(games))
    game = games[game_decision - 1]
    print(f'Nice one! {game["game_name"]} is a great game!')
    difficulty = get_int_user_decision(
        f'Please set difficulty level from 1 to {game["game_difficulty"].stop - 1}:',
        int(game["game_difficulty"].stop - 1)
    )
    print(f'''The difficulty level you have chosen is: {difficulty}
    Oo. That's it for now! See you on the next stage of the project! .oO''')


# welcome()
start_play()
