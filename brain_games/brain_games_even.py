import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")


def is_number_even():

    print('Answer "yes" if the number is even, otherwise answer "no".')  # game rule
    correct_answers_counter = 0
    while correct_answers_counter < 3:

        even_game_number = randint(1, 100)

        correct_answer = 'yes'
        incorrect_answer = 'no'

        if even_game_number % 2 != 0:
            correct_answer, incorrect_answer = incorrect_answer, correct_answer

        print(f'Question: {even_game_number}')
        user_answer = prompt.string('Your answer: ')
        while user_answer.lower() not in ['yes', 'no']:
            user_answer = prompt.string(f'You should answer "yes" or "no", so is {even_game_number} even number? ')

        if user_answer.lower() == correct_answer:
            print('Correct!')
            correct_answers_counter += 1

        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user_name}!")
            correct_answers_counter = 0

    print('')
    print(f'Congratulatios, {user_name}!')
