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
    """Generate and return progression."""
    progression_length = random.randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = []
    element = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    while len(progression) <= progression_length:
        progression.append(element)
        element += step
    return (progression, progression_length)


def run_round():
    """Return variables for game logic."""
    progression, progression_length = make_progression()
    question_index = random.randint(0, progression_length - 1)
    right_answer = str(progression[question_index])
    progression[question_index] = '..'
    question = (' '.join(map(str, progression)))
    return (question, right_answer)


if __name__ == '__main__':
    run_round()
