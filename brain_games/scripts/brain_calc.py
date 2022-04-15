#!/usr/bin/env python

"""Calc game launch."""

from brain_games import game_logic


def main():
    """Play calculator game."""
    game_name = 'calc'
    game_logic.logic(game_name)


if __name__ == '__main__':
    main()
