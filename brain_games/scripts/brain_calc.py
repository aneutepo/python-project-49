import random
from brain_games.cli import welcome_user
from brain_games.check_user_answer import check_user_answer


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
    return math_question, correct_answer, user_answer


def get_correct_answer(first_number, second_number, math_sign):
    if math_sign == "+":
        return first_number + second_number
    elif math_sign == "-":
        return first_number - second_number
    else:
        return first_number * second_number


def calc():
    score = 0
    username = welcome_user()
    print("What is the result of the expression?")
    while True:
        math_question, correct_answer, user_answer = create_question()

        if check_user_answer(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == '__main__':
    calc()
