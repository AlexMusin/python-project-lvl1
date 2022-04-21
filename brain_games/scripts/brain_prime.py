#!/usr/bin/env python
"""Prime game launch."""

from brain_games import game_logic
from brain_games.games import prime


def main():
    """Play prime game."""
    game_logic.run(prime)


if __name__ == '__main__':
    main()
