import random
from brain_games.cli import welcome_user


def main():
    number_correct_answers = 0
    username = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while True:
        question_number = random.randint(1, 10000)
        print(f"Question: {question_number}")
        answer = input("Your answer: ")
        if question_number % 2 == 0:
            if answer == 'yes':
                print("Correct!")
                number_correct_answers += 1
            else:
                print(f"Answer '{answer}' is wrong answer ;(. ", end='')
                print("Correct answer was 'yes'.")
                print(f"Let's try again, {username}!")
                break
        else:
            if answer == 'no':
                print("Correct!")
                number_correct_answers += 1
            else:
                print(f"Answer '{answer}' is wrong answer ;(. ", end='')
                print("Correct answer was 'no'.")
                print(f"Let's try again, {username}!")
                break
        if number_correct_answers == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == "__main__":
    main()
