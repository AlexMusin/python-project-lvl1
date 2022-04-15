"""Prime game."""

import random

import prompt

LEFT_LIMIT = 1
RIGHT_LIMIT = 53
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    """Return variables for game logic."""
    given_number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    is_prime = 1
    index = 2
    modifier = 2 if given_number < 3 else 0
    while is_prime == 1 and index <= int(given_number / 2) + modifier:
        if not given_number % index:
            is_prime = 0
        index += 1
    cond = 'yes' if is_prime else 'no'
    print('Question: {0}'.format(given_number))
    answer = prompt.string('Your answer: ')
    return (cond, answer)


if __name__ == '__main__':
    run_game()
