#!/usr/bin/env python
"""Ask username and return greeting."""

import prompt


def welcome_user():
    """Ask username."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


def main():
    """Define main func."""
    welcome_user()


if __name__ == '__main__':
    main()
