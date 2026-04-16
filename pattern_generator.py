"""
pattern_generator.py - Generates ASCII patterns for MemoryMaster pictures mode.

This module creates grids of random characters that the player
has to memorize and type back.
"""

import random

SYMBOLS = ["#", "@", "*", "+", "=", "%", "&", "?", "!", "~"]


def generate_pattern(rows, cols):
    """
    Create a grid of random symbols as a list of strings.

    Each string in the list is one row of the pattern.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of characters in each row.

    Returns:
        list: A list of strings where each string is one row.

    Raises:
        ValueError: If rows or cols is less than 1.
    """
    pass


def format_pattern(pattern):
    """
    Turn a pattern into a readable string with spaces between characters.

    Args:
        pattern (list): A list of row strings from generate_pattern.

    Returns:
        str: The pattern formatted with spaces, ready to print.
    """
    pass


def check_pattern_answer(target, answer):
    """
    Check if the player correctly reproduced the pattern.

    Spaces are ignored so "# @" and "#@" both count as the same row.

    Args:
        target (list): The original pattern list shown to the player.
        answer (str): What the player typed (multiple lines).

    Returns:
        bool: True if the pattern matches, False otherwise.
    """
    pass


def get_pattern_size(level):
    """
    Figure out how big the pattern grid should be for a given level.

    Levels 1-3 use one row that gets wider.
    After level 3, more rows are added as the level goes up.

    Args:
        level (int): The current game level.

    Returns:
        tuple: A (rows, cols) pair.

    Raises:
        ValueError: If level is less than 1.
    """
    pass