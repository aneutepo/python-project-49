import random
from brain_games.cli import welcome_user


def get_answer(first_number, second_number, math_sign):
    if math_sign == "+":
        return first_number + second_number
    elif math_sign == "-":
        return first_number - second_number
    else:
        return first_number * second_number


def calc():
    massive_of_signs = ['+', '-', '*']
    score = 0
    username = welcome_user()
    print("What is the result of the expression?")
    while True:
        first_number = random.randint(1, 6)
        second_number = random.randint(1, 6)
        math_sign = random.choice(massive_of_signs)
        math_question = f"{str(first_number)} {math_sign} {str(second_number)}"
        print(f"Question: {math_question}")
        user_answer = input("Your answer: ")
        correct_answer = get_answer(first_number, second_number, math_sign)

        if user_answer == str(correct_answer):
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {username}!")
            break

        if score == 3:
            print(f"Congratulations, {username}")
            break


if __name__ == '__main__':
    calc()
