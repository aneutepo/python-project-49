import prompt
MAX_ROUNDS = 3


def game_process(game):
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}")
    print(game.RULES)
    for _ in range(MAX_ROUNDS):
        correct_answer, question = game.game_data()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
