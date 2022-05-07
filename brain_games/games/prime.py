"""Prime game."""

import math
import random

LEFT_LIMIT = 1
RIGHT_LIMIT = 53
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Decide if given number is prime or not. Return boolean."""
    for divisor in range(2, int(math.sqrt(number)) + 2):
        if not number % divisor:
            return (False)
    return (True)


def run_round():
    """Return variables for game logic."""
    number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    right_answer = 'yes' if is_prime(number) else 'no'
    return (number, right_answer)
