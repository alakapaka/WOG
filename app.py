import os


def get_int_user_decision(opening_msg, limit = int()):
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


def create_game_option(game_name, game_desc, difficulty_lvl_max):
    return {
        "game_name": game_name,
        "game_desc": game_desc,
        "game_difficulty": range(1, difficulty_lvl_max + 1)
    }


def get_games():
    return [
        create_game_option('Memory Game',
                           'a sequence of numbers will appear for 1 second and you have to guess it back.',
                           5),
        create_game_option('Guess Game',
                           'guess a number and see if you chose like the computer.',
                           5
                           ),
        create_game_option('Currency Roulette',
                           'try and guess the value of a random amount of USD in ILS.',
                           5
                           )
    ]


def print_games(games):
    opening_msg = 'Please choose a game to play:'
    games_txt = ''
    for game in games:
        games_txt = games_txt + (f'{games.index(game) + 1}. '
                                 f'{games[games.index(game)]["game_name"]} - '
                                 f'{games[games.index(game)]["game_desc"]}\n')
    return opening_msg + '\n' + games_txt
