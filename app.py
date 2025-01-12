import importlib

import utils


def welcome():
    username = get_str_user_decision('Please insert your name:', 1, True)
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    while True:
        games = get_games()
        game_decision = get_int_user_decision(print_games(games), len(games))
        game = games[game_decision - 1]
        game_file = game['game_file']
        loaded_game = importlib.import_module(f'game_modules.{game_file}')
        print(f'Nice one! {game["game_name"]} is a great game!')
        difficulty = get_int_user_decision(
            f'Please set difficulty level from 1 to {game["game_difficulty"].stop - 1}:',
            int(game["game_difficulty"].stop - 1)
        )
        print(f'''The difficulty level you have chosen is: {difficulty}''')
        loaded_game.play(difficulty)
        continue_game = get_bool_user_decision('Would you like to play another game? (Y/N)')
        if continue_game:
            utils.screen_cleaner()
            continue
        else:
            utils.screen_cleaner()
            print('Goodbye! press enter to exit')
            input()
            break


def get_int_user_decision(opening_msg, limit=int()):
    while True:
        print(opening_msg)
        decision = input()
        if not decision.isnumeric():
            print(f'Please insert a valid * NUMBER * between 1 to {limit}')
            continue
        decision = int(decision)
        if limit < decision or decision == 0:
            print(f'Please insert a valid number between 1 to {limit}')
            continue
        break
    return decision


def get_str_user_decision(opening_msg, min_characters, str_only=False):
    while True:
        print(opening_msg)
        decision = input()
        if len(decision.strip()) <= 1:
            print(f" !- Name must be longer than {min_characters} character(s). -!")
            continue
        if str_only and any(map(str.isdigit, decision)):
            print(" !- Name must not contain digits -!")
            continue
        break
    return decision


def get_bool_user_decision(opening_msg):
    while True:
        print(opening_msg)
        decision = input()
        if len(decision.strip()) >= 2 or len(decision.strip()) > 1:
            print(f" !- Please insert Y/N -!")
            continue
        if any(map(str.isdigit, decision)):
            print(f" !- Please insert Y/N -!")
            continue
        if decision.isspace() or decision == '':
            print(f" !- Please insert Y/N -!")
            continue
        if not decision.capitalize() == 'Y' and not decision.capitalize() == 'N':
            print(f" !- Please insert Y/N -!")
            continue
        break
    return decision.capitalize() == 'Y'


def create_game_option(game_name, game_desc, difficulty_lvl_max, game_file):
    return {
        "game_name": game_name,
        "game_desc": game_desc,
        "game_difficulty": range(1, difficulty_lvl_max + 1),
        "game_file": game_file
    }


def get_games():
    return [
        create_game_option('Memory Game',
                           'a sequence of numbers will appear for 1 second and you have to guess it back.',
                           5,
                           'memory_game'),
        create_game_option('Guess Game',
                           'guess a number and see if you chose like the computer.',
                           5,
                           'guess_game'),
        create_game_option('Currency Roulette',
                           'try and guess the value of a random amount of USD in ILS.',
                           5,
                           'currency_roulette_game')
    ]


def print_games(games):
    opening_msg = 'Please choose a game to play:'
    games_txt = ''
    for game in games:
        games_txt = games_txt + (f'{games.index(game) + 1}. '
                                 f'{games[games.index(game)]["game_name"]} - '
                                 f'{games[games.index(game)]["game_desc"]}\n')
    return opening_msg + '\n' + games_txt
