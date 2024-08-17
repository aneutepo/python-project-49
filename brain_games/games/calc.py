import random
from brain_games.game_title import GAME_TITLES
from brain_games.game_engine import game_process


def generate_game_data():
    massive_of_signs = ['+', '-', '*']
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    math_sign = random.choice(massive_of_signs)
    math_question = f"{str(first_number)} {math_sign} {str(second_number)}"
    print(f"Question: {math_question}")
    user_answer = input("Your answer: ")
    if math_sign == "+":
        correct_answer = first_number + second_number
    elif math_sign == "-":
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return correct_answer, user_answer


def calc_game():
    game_process(generate_game_data, GAME_TITLES['calc'])
