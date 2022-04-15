#!/usr/bin/env python
"""Prime game launch."""

from brain_games import game_logic


def main():
    """Play prime game."""
    game_name = 'prime'
    game_logic.logic(game_name)


if __name__ == '__main__':
    main()
