from random import randint


task = 'What number is missing in the progression?'


def game_options():
    progression_step = randint(2, 10)
    progression_start = randint(1, 100)
    progression_length = 10
    nums_counter = 0
    nums = []

    while nums_counter < progression_length:
        nums.append(str(progression_start + progression_step * nums_counter))
        nums_counter += 1
    changing_index = randint(1, progression_length - 1)
    correct_answer = nums[changing_index]
    nums[changing_index] = '..'
    progression_row = ' '.join(nums)
    return progression_row, correct_answer
