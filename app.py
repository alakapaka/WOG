import os


def welcome():
    print('Please insert your name:')
    username = input()
    if len(username) <= 1:
        print(" !- Name must be longer than one letter. -!")
        welcome()
    else:
        print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play(user_input=input()):
    games = get_games()
    print('Please choose a game to play:')
    for game in games:
        print(f'{games.index(game) + 1}. '
              f'{games[games.index(game)]["game_name"]} - {games[games.index(game)]["game_desc"]}')
    game_decision = get_int_user_decision(len(games))
    print(f'Nice one! {games[int(game_decision) - 1]["game_name"]} is a great game!')
    print(f'Please set difficulty level from 1 to {games[int(game_decision) - 1]["game_difficulty"].stop - 1}:')
    difficulty = get_int_user_decision(int(games[int(game_decision) - 1]["game_difficulty"].stop - 1))
    print(f'The difficulty level you choose is: {difficulty}')
    print(f"\n Oo. That's it for now! See you on the next stage of the project! .oO")


def get_int_user_decision(limit):
    decision = input()
    if not decision.isnumeric():
        print(f'Please insert a valid * NUMBER * between 1 to {limit}')
        return get_int_user_decision(limit)
    elif int(limit) < int(decision) or int(decision) == 0:
        print(f'Please insert a valid number between 1 to {limit}')
        return get_int_user_decision(limit)
    else:
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
