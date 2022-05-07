"""Progression game."""

import random

RULES = 'What number is missing in the progression?'
LEFT_LIMIT = -25
RIGHT_LIMIT = 25
PROGR_LENGTH_MIN = 5
PROGR_LENGTH_MAX = 12
STEP_MIN = -10
STEP_MAX = 10


def run_round():
    """Return variables for game logic."""
    progression_length = random.randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    element = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    progression = ''
    counter = 0
    question_index = random.randint(0, progression_length - 1)
    while counter + 1 <= progression_length:
        if counter == question_index:
            progression = f'{progression} ..'
            right_answer = str(element)
        else:
            progression = f'{progression} {element}'
        element += step
        counter += 1
    return (progression, right_answer)
