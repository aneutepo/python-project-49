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


def main():
    username = welcome_user()
    score = 0
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    while True:
        question_number = random.randint(1, 10)
        print(f"Question: {question_number}")
        user_ans = input("Your answer: ")
        correct_answer = prime_number_check(question_number)
        if user_ans == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"'{user_ans}' is wrong answer ;(. ", end='')
            print("Correct answer was ", end='')
            print(f"'{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == '__main__':
    main()
