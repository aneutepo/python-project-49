import random
from brain_games.game_engine import game_process
from brain_games.game_title import GAME_TITLES


def create_question():
    question_number = random.randint(1, 10)
    print(f"Question: {question_number}")
    user_ans = input("Your answer: ")
    if question_number <= 1:
        correct_answer = "no"
    elif question_number == 2:
        correct_answer = "yes"
    else:
        correct_answer = "yes"
        for i in range(2, int(question_number ** 0.5) + 1):
            if question_number % i == 0:
                correct_answer = "no"
                break
    return correct_answer, user_ans


def prime_game():
    game_process(create_question, GAME_TITLES['prime'])
