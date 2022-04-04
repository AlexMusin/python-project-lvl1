#!/usr/bin/env python
"""Brain-games main script."""

from brain_games import cli


def say_welcome():
    """Say Welcome."""
    return ('Welcome to the Brain Games!')


def main():
    """Define main function."""
    print(say_welcome())
    cli.welcome_user()


if __name__ == '__main__':
    main()
