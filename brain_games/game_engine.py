import prompt


def game_process(generate_question_and_answer, game_title):
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}")
    print(game_title)
    score = 0
    while True:
        correct_answer, user_answer = generate_question_and_answer()
        if user_answer == str(correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break
