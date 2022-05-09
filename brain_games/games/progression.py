"""Progression game."""

import random

RULES = 'What number is missing in the progression?'
LEFT_LIMIT = -25
RIGHT_LIMIT = 25
PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 12
STEP_MIN = -10
STEP_MAX = 10


def run_round():
    """Return variables for game logic."""
    progression_length = random.randint(
        PROGRESSION_MIN_LENGTH, PROGRESSION_MAX_LENGTH,
    )
    step = random.randint(STEP_MIN, STEP_MAX)
    element = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    progression = []
    for _ in range(progression_length):
        progression.append(str(element))
        element += step
    random_index = random.randint(0, progression_length - 1)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    progression = ' '.join(progression)
    return (progression, right_answer)
