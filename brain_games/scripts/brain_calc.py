import random
from brain_games.get_username import get_username
from brain_games.check_user_answer import check_user_answer


def game_process():
    score = 0
    username = get_username()
    while True:
        correct_answer, user_answer = create_question()
        if check_user_answer(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


def create_question():
    massive_of_signs = ['+', '-', '*']
    first_number = random.randint(1, 6)
    second_number = random.randint(1, 6)
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


def calc():
    print("What is the result of the expression?")
    game_process()


if __name__ == '__main__':
    calc()
