import random
from math import gcd
from brain_games.cli import welcome_user


def create_question():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    print(f"Question: {first_number} {second_number}")
    user_answer = input("Your answer: ")
    correct_answer = gcd(first_number, second_number)
    return user_answer,correct_answer


def check_user_answer(correct_answer, user_answer, username):
    if user_answer == str(correct_answer):
        print("Correct!")
        return True
    else:
        print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {username}!")
        return False
    

def main():
    username = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    score = 0
    while True:
        user_answer, correct_answer = create_question()
        if check_user_answer(correct_answer,user_answer,username):
            score += 1
        else:
            break

        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == "__main__":
    main()
