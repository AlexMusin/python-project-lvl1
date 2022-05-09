"""Ask username and return greeting."""

import prompt


def welcome_user():
    """Ask username."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
