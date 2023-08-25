#!/usr/bin/env python3

from brain_games.bg_engine import start_game
from brain_games.games import bg_progression_logic


def main():
    start_game(bg_progression_logic)


if __name__ == '__main__':
    main()
