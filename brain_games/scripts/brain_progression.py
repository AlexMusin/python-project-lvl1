#!/usr/bin/env python
"""Progression game launch."""

from brain_games import game_logic


def main():
    """Play gcd game."""
    game_name = 'progression'
    game_logic.logic(game_name)


if __name__ == '__main__':
    main()
