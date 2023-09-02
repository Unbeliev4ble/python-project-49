from random import randint


TASK = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_gcd(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def get_question_and_answer():
    num_1 = randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = str(get_gcd(num_1, num_2))
    question = f'{num_1} {num_2}'
    return question, correct_answer
