import random
from brain_games.cli import welcome_user


def prime_number_check(number):
    if number <= 1:
        return "no"
    if number == 2:
        return "yes"
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


def create_question():
    question_number = random.randint(1, 10)
    print(f"Question: {question_number}")
    user_ans = input("Your answer: ")
    correct_answer = prime_number_check(question_number)
    return correct_answer, user_ans


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
    score = 0
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    while True:
        correct_answer, user_answer = create_question()
        if check_user_answer(correct_answer, user_answer, username):
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print("Correct answer was ", end='')
            print(f"'{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == '__main__':
    main()
