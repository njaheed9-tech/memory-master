"""
pattern_generator.py - Generates ASCII patterns for MemoryMaster pictures mode. naveed test
"""

import random

SYMBOLS = ["#", "@", "*", "+", "=", "%", "&", "?", "!", "~"]


def generate_pattern(rows, cols):
    """Create a grid of random symbols as a list of strings."""
    if rows < 1 or cols < 1:
        raise ValueError("rows and cols must be at least 1")
    pattern = []
    for i in range(rows):
        row = ""
        for j in range(cols):
            row += random.choice(SYMBOLS)
        pattern.append(row)
    return pattern 


def format_pattern(pattern):
    """Return the pattern as a printable string with spaces between characters."""
    result = ""
    for row in pattern:
        result += " ".join(row) + "\n"
        return result.strip()


def check_pattern_answer(target, answer):
    """Return True if the player's answer matches the pattern, False if not."""
    answer_rows = answer.strip()
    answer_rows = [row.replace("")]
    target_rows = [row.replace(" ", "")]
    return answer_rows == target_rows # check if they match 


def get_pattern_size(level):
    """Return the (rows, cols) grid size for a given level."""
    if level < 1: 
        raise ValueError("level must be at least 1")
    if level <= 3: 
        return(1)