from brain_games.game_engine import game_process
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES


def create_question():
    question_number = generate_random_number()
    print(f"Question: {question_number}")
    user_ans = input("Your answer: ")
    if question_number <= 1:
        correct_answer = "no"
    if question_number == 2:
        correct_answer = "yes"
    for i in range(2, question_number):
        if question_number % i == 0:
            correct_answer = "no"
    return correct_answer, user_ans


def prime_game():
    game_process(create_question, GAME_TITLES['prime'])
