from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_number_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_number_even(question_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_number, correct_answer
