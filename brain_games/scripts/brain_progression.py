#!/usr/bin/env python
"""Progression game launch."""

from brain_games import game_logic
from brain_games.games import progression


def main():
    """Play gcd game."""
    game_logic.run(progression)


if __name__ == '__main__':
    main()
