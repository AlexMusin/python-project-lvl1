"""Progression game."""

import random

RULES = 'What number is missing in the progression?'
LEFT_LIMIT = -25
RIGHT_LIMIT = 25
PROGR_LENGTH_MIN = 5
PROGR_LENGTH_MAX = 12
STEP_MIN = -10
STEP_MAX = 10


def make_progression():
    """Generate and return progression and right_answer."""
    progression_length = random.randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    element = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    progression = []
    while len(progression) <= progression_length:
        progression.append(element)
        element += step
    question_index = random.randint(0, progression_length - 1)
    right_answer = str(progression[question_index])
    progression[question_index] = '..'
    progression = ' '.join(map(str, progression))
    return (progression, right_answer)


def run_round():
    """Return variables for game logic."""
    return (make_progression())


if __name__ == '__main__':
    run_round()
