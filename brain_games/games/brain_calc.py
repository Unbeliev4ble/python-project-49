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

    first_num = random.randint(1, 10)
    second_num = random.randint(1, 12)
    expression = f"{first_num} {picked_operator} {second_num}"
    correct_answer = operator_functions[picked_operator](first_num, second_num)
    print(correct_answer)

    return expression, correct_answer
#
print(game_options())