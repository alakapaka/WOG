import random
from time import sleep
import score
import utils


def generate_sequence(dif_lvl):
    sequence = []
    list_length = dif_lvl + 1
    while list_length > 0:
        sequence.append(random.randint(1, 101))
        list_length -= 1
    return sequence


def get_list_from_user(dif_lvl):
    list_length = dif_lvl + 1
    print(f'Enter {list_length} numbers:')
    user_list = []
    while list_length > 0:
        while True:
            decision = input()
            if not decision.isnumeric():
                print(f'Please insert a valid * NUMBER * between 1 to 101')
                continue
            decision = int(decision)
            if decision > 101 or decision <= 0:
                print(f'Please insert a valid * NUMBER * between 1 to 101')
                continue
            break
        user_list.append(decision)
        if list_length > 1:
            print('Enter the next number:')
        list_length -= 1
    return user_list


def is_list_equal(original_list, user_list):
    return original_list == user_list


def play(dif_lvl):
    original_list = generate_sequence(dif_lvl)
    print('You have 3 seconds to remember the following sequence, press enter to view it.')
    input()
    utils.screen_cleaner()
    print(original_list)
    sleep(3)
    utils.screen_cleaner()
    if is_list_equal(original_list, get_list_from_user(dif_lvl)):
        score.add_score(dif_lvl)
    else:
        print(f'''Too Bad! That's wrong :( the sequence was: {original_list}''')
