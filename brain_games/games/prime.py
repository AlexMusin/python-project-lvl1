"""Prime game."""

import random

LEFT_LIMIT = 1
RIGHT_LIMIT = 53
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def detect_prime(given_number):
    """Decide if given number is prime or not. Return 0 or 1."""
    is_prime = 1
    index = 2
    while is_prime == 1 and index <= int(given_number / 2):
        if not given_number % index:
            is_prime = 0
        index += 1
    return (is_prime)


def run_game():
    """Return variables for game logic."""
    given_number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    right_answer = 'yes' if detect_prime(given_number) else 'no'
    return (given_number, right_answer)


if __name__ == '__main__':
    run_game()
