import random

import score


def generate_number(dif_lvl):
    return random.randint(0, dif_lvl)


def get_guess_from_user(dif_lvl):
    while True:
        print(f'Guess a number between 0 and {dif_lvl}')
        decision = input()
        if not decision.isnumeric():
            print(f'Please insert a valid * NUMBER * between 0 to {dif_lvl}')
            continue
        decision = int(decision)
        if dif_lvl < decision or decision < 0:
            print(f'Please insert a valid number between 0 to {dif_lvl}')
            continue
        break
    return decision


def compare_results(secret_number, user_decision):
    return secret_number == user_decision


def play(dif_lvl):
    secret_number = generate_number(dif_lvl)
    if compare_results(secret_number, get_guess_from_user(dif_lvl)):
        score.add_score(dif_lvl)
    else:
        print(f'''Too Bad! That's wrong :( the secret number was: {secret_number}''')
