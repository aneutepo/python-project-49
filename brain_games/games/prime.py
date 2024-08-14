from brain_games.get_username import get_username
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES
from brain_games.write_answer_text import write_answer_text


def create_question():
    question_number = generate_random_number()
    print(f"Question: {question_number}")
    user_ans = input("Your answer: ")
    correct_answer = prime_number_check(question_number)
    return correct_answer, user_ans


def prime_number_check(number):
    if number <= 1:
        return "no"
    if number == 2:
        return "yes"
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


def game_process():
    score = 0
    username = get_username()
    print(GAME_TITLES['prime'])
    while True:
        correct_answer, user_answer = create_question()
        if write_answer_text(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break
