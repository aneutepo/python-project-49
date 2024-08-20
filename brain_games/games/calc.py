import random
RULES = "What is the result of the expression?"


def game_data():
    massive_of_signs = ['+', '-', '*']
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    math_sign = random.choice(massive_of_signs)
    question = f"{str(first_number)} {math_sign} {str(second_number)}"
    if math_sign == "+":
        correct_answer = first_number + second_number
    elif math_sign == "-":
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return correct_answer, question
