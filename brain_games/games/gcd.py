from math import gcd
from brain_games.get_username import get_username
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES
from brain_games.write_answer_text import write_answer_text


def create_question():
    first_number = generate_random_number()
    second_number = generate_random_number()
    print(f"Question: {first_number} {second_number}")
    user_answer = input("Your answer: ")
    correct_answer = gcd(first_number, second_number)
    return user_answer, correct_answer


def game_process():
    score = 0
    username = get_username()
    print(GAME_TITLES['gcd'])
    while True:
        user_answer, correct_answer = create_question()
        if write_answer_text(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break
