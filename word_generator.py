"""
word_generator.py - Generates word lists for MemoryMaster phrases mode.

This module picks random words from a list that the player
has to remember in order.
"""

import random

WORD_POOL = [
    "apple", "bridge", "candle", "dragon", "engine",
    "forest", "garden", "hammer", "island", "jungle",
    "kettle", "lantern", "marble", "needle", "orange",
    "pillow", "ribbon", "silver", "tunnel", "umbrella",
    "velvet", "window", "anchor", "basket", "carpet",
    "desert", "eagle", "feather", "goblin", "harbor",
    "jacket", "knight", "ladder", "magnet", "napkin",
    "oyster", "pencil", "rabbit", "saddle", "throne",
    "walrus", "yogurt", "canvas", "donkey", "fossil",
]


def generate_word_list(count):
    """
    Return a list of random unique words.

    Args:
        count (int): How many words to include. Must be at least 1.

    Returns:
        list: A list of randomly chosen words with no repeats.

    Raises:
        ValueError: If count is less than 1.
    """
    pass


def check_word_list_answer(target, answer):
    """
    Check if the player typed the words back in the right order.

    This is case-insensitive so "Apple" and "apple" both count.

    Args:
        target (list): The original list of words shown to the player.
        answer (str): What the player typed.

    Returns:
        bool: True if the words match in order, False otherwise.
    """
    pass