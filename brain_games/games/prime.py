from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_number_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    question_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_number_prime(question_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_number, correct_answer
