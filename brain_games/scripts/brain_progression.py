#!/usr/bin/env python
"""Progression game launch."""

from brain_games import game_logic
from brain_games.games import game_progression


def main():
    """Play gcd game."""
    game_logic.logic(game_progression)


if __name__ == '__main__':
    main()
