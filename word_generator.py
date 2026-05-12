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
        ValueError: If count is less than 1 or greater than the word pool size.
    """
    if count < 1:
        raise ValueError("Count must be at least 1")
    if count > len(WORD_POOL):
        raise ValueError(f"Count cannot exceed {len(WORD_POOL)} words")
    return random.sample(WORD_POOL, count)


def check_word_list_answer(target, answer):
    """
    Check if the player typed the words back in the right order.

    This is case-insensitive so "Apple" and "apple" both count.
    Extra spaces are handled automatically.

    Args:
        target (list): The original list of words shown to the player.
        answer (str): What the player typed.

    Returns:
        bool: True if the words match in order, False otherwise.
    """
    # Handle empty or whitespace-only answers
    if not answer or not answer.strip():
        return False
    
    # Split on whitespace (handles multiple spaces, tabs, etc.)
    player_words = answer.strip().lower().split()
    correct_words = [word.lower() for word in target]
    
    # Check if the number of words matches
    if len(player_words) != len(correct_words):
        return False
    
    return player_words == correct_words