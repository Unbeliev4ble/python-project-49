import operator
import random


task = 'What is the result of the expression?'


def game_options():
    operator_list = ['*', '+', '-']
    operator_functions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        }
    picked_operator = random.choice(operator_list)

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 12)
    expression = f"{num_1} {picked_operator} {num_2}"
    correct_answer = str(operator_functions[picked_operator](num_1, num_2))
    return expression, correct_answer
