"""Progression game."""

import random

RULES = 'What number is missing in the progression?'
LEFT_LIMIT = -25
RIGHT_LIMIT = 25
PROGRESSION_LENGTH_MIN = 5
PROGRESSION_LENGTH_MAX = 12
STEP_MIN = -10
STEP_MAX = 10


def make_progression():
    """Generate and return progression."""
    progression_length = random.randint(PROGRESSION_LENGTH_MIN, PROGRESSION_LENGTH_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = []
    element = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    while len(progression) <= progression_length:
        progression.append(element)
        element += step
    return (progression, progression_length)


def run_game():
    """Return variables for game logic."""
    progression, progression_length = make_progression()
    q_index = random.randint(0, progression_length - 1)
    condition = str(progression[q_index])
    progression[q_index] = '..'
    question = (' '.join(map(str, progression)))
    return (question, condition)


if __name__ == '__main__':
    run_game()
