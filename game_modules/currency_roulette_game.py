import random
import requests

import score


def get_money_interval(multiplier):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            return response_json['rates']['ILS'] * multiplier
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def get_guess_from_user(multiplier):
    while True:
        print(f'Guess how much is {multiplier} USD in ILS:')
        decision = input()
        if not decision.replace('.', '').isdecimal():
            print(f'Please insert a valid * DECIMAL * ')
            continue
        decision = float(decision)
        if decision <= 0.0:
            print(f'Please insert a valid decimal bigger than 0')
            continue
        break
    return decision


def compare_results(interval, dif_lvl, user_decision):
    allowed_difference = 10 - dif_lvl
    difference = interval - user_decision
    if difference < 0:
        difference *= -1
    return difference <= allowed_difference


def play(dif_lvl):
    multiplier = random.randint(1, 100)
    interval = get_money_interval(multiplier)
    if compare_results(interval, dif_lvl, get_guess_from_user(multiplier)):
        score.add_score(dif_lvl)
    else:
        print(f'''Too Bad! That's wrong :( the correct answer was: {interval}''')
