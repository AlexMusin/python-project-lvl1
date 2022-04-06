#!/usr/bin/env python
"""Choose even game."""

import random
import sys

import prompt


def error():
    """Say error."""
    incorrect = 'Incorrect!\nPlease run the game again'
    sys.exit(incorrect)


def main():
    """Play odd-or-even game."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    greet = ('Hello, {0}'.format(username))
    print(greet)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    right_limit = -256
    left_limit = 255
    while index < 3:
        number = random.randint(right_limit, left_limit)    # noqa: S311
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            answer = 1
        elif answer == 'no':
            answer = 0
        else:
            error()
        is_even = number % 2 == 0
        if (is_even == answer):
            print('Correct!')
            index += 1
        else:
            error()
    if index == 3:
        print('Congratulations, {0}!'.format(username))


if __name__ == '__main__':
    main()
