from brain_games.get_username import get_username
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES
from brain_games.write_answer_text import write_answer_text


def create_question():
    question_number = generate_random_number()
    print(f"Question: {question_number}")
    user_answer = input("Your answer: ")
    correct_answer = get_correct_answer(question_number)
    return correct_answer, user_answer


def get_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_process():
    score = 0
    username = get_username()
    print(GAME_TITLES['even'])
    while True:
        correct_answer, user_answer = create_question()
        if write_answer_text(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break
