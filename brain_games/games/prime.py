"""Prime game."""

import math
import random

LEFT_LIMIT = 1
RIGHT_LIMIT = 53
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Decide if given number is prime or not. Return 0 or 1."""
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if not number % divisor:
            return (False)
    return (True)


def run_round():
    """Return variables for game logic."""
    given_number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    right_answer = 'yes' if is_prime(given_number) else 'no'
    return (given_number, right_answer)


if __name__ == '__main__':
    run_round()
