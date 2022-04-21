"""Progression game."""

import random

import prompt

RULES = 'What number is missing in the progression?'
LEFT_LIMIT = -25
RIGHT_LIMIT = 25
PROGR_LENGTH_MIN = 5
PROGR_LENGTH_MAX = 12
STEP_MIN = -10
STEP_MAX = 10


def make_progression():
    """Generate and return progression."""
    progr_length = random.randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)
    q_index = random.randint(0, progr_length - 1)
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = []
    element = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    while len(progression) <= progr_length:
        progression.append(element)
        element += step
    cond = str(progression[q_index])
    progression[q_index] = '..'
    progression = (' '.join(map(str, progression)))
    return (progression, cond)


def run_game():
    """Return variables for game logic."""
    progression, cond = make_progression()
    print('Question: {0}'.format(progression))
    answer = prompt.string('Your answer: ')
    return (cond, answer)


if __name__ == '__main__':
    run_game()
