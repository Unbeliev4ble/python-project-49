from random import randint, choice


TASK = 'What number is missing in the progression?'
INITIAL_TERM_MIN = 1
INITIAL_TERM_MAX = 100
COMMON_DIFFERENCE_MIN = 2
COMMON_DIFFERENCE_MAX = 10
TERMS_QUANTITY_MIN = 10
TERMS_QUANTITY_MAX = 15


def generate_progression(initial_term, common_difference, terms_quantity):
    terms_counter = 0
    progression = []
    while terms_counter < terms_quantity:
        progression.append(initial_term + common_difference * terms_counter)
        terms_counter += 1
    return progression


def hide_element(sequence, element_index):
    hidden_element = sequence[element_index]
    sequence[element_index] = '..'
    string_sequence = ' '.join(str(i) for i in sequence)
    return string_sequence, str(hidden_element)


def get_question_and_answer():
    initial_term = randint(INITIAL_TERM_MIN, INITIAL_TERM_MAX)
    common_difference = randint(COMMON_DIFFERENCE_MIN, COMMON_DIFFERENCE_MAX)
    terms_quantity = randint(TERMS_QUANTITY_MIN, TERMS_QUANTITY_MAX)

    progression = \
        (generate_progression(initial_term, common_difference, terms_quantity))

    hidden_element_index = choice(range(len(progression)))

    question, correct_answer = hide_element(progression, hidden_element_index)
    return question, correct_answer
