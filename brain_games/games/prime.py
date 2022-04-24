"""Prime game."""

import random

LEFT_LIMIT = 1
RIGHT_LIMIT = 53
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def detect_prime(given_number):
    """Decide if given number is prime or not. Return 0 or 1."""
    is_prime = 1
    for divisor in range(2, given_number // 2 + 1):
        if not given_number % divisor:
            is_prime = 0
            break
    return (is_prime)


def run_round():
    """Return variables for game logic."""
    given_number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    right_answer = 'yes' if detect_prime(given_number) else 'no'
    return (given_number, right_answer)


if __name__ == '__main__':
    run_round()
