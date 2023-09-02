import operator
import random


TASK = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10


def get_question_and_answer():
    operator_list = ['*', '+', '-']
    operator_functions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    picked_operator = random.choice(operator_list)

    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{num_1} {picked_operator} {num_2}"
    correct_answer = str(operator_functions[picked_operator](num_1, num_2))
    return question, correct_answer
