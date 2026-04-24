"""
main.py - Entry point for MemoryMaster.

Run this file to start the game:
    python main.py
"""

from game import MemoryMasterGame


def get_mode():
    """
    Ask the player to pick a game mode and return their choice.

    Returns:
        str: 'numbers', 'phrases', or 'pictures'
    """
    pass


def get_difficulty():
    """
    Ask the player to pick a difficulty and return their choice.

    Returns:
        str: 'easy', 'medium', or 'hard'
    """
    pass


if __name__ == "__main__":
    mode = get_mode()
    difficulty = get_difficulty()

    game = MemoryMasterGame(mode=mode, difficulty=difficulty)
    game.run()
