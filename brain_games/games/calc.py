import random
from brain_games.get_username import get_username
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES
from brain_games.write_answer_text import write_answer_text


def create_question():
    massive_of_signs = ['+', '-', '*']
    first_number = generate_random_number()
    second_number = generate_random_number()
    math_sign = random.choice(massive_of_signs)
    math_question = f"{str(first_number)} {math_sign} {str(second_number)}"
    print(f"Question: {math_question}")
    user_answer = input("Your answer: ")
    correct_answer = get_correct_answer(first_number,
                                        second_number, math_sign)
    return correct_answer, user_answer


def get_correct_answer(first_number, second_number, math_sign):
    if math_sign == "+":
        return first_number + second_number
    elif math_sign == "-":
        return first_number - second_number
    else:
        return first_number * second_number


def game_process():
    score = 0
    username = get_username()
    print(f"{GAME_TITLES['calc']}")
    while True:
        correct_answer, user_answer = create_question()
        if write_answer_text(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break
