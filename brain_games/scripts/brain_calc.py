#!/usr/bin/env python

"""Calc game launch."""

from brain_games import game_logic
from brain_games.games import calc


def main():
    """Play calculator game."""
    game_logic.run_logic(calc)


if __name__ == '__main__':
    main()
