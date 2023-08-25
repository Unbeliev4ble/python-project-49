import prompt


ROUNDS_TO_WIN = 3


def start_game(game_logic):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")

    print(f"{game_logic.task}")

    correct_answers_counter = 0
    while correct_answers_counter < ROUNDS_TO_WIN:
        expression, correct_answer = game_logic.game_options()
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_counter += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f' Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user_name}!")
            return
    print('')
    print(f'Congratulations, {user_name}!')
