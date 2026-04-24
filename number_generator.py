"""
number_generator.py - Generates random numbers for MemoryMaster.

This module handles creating random numbers of different lengths
depending on what level the player is on.
"""

import random


def generate_number(digits):
    """
    Generate a random number string with a given number of digits.

    The first digit will never be 0 so the number always has
    the right amount of digits.

    Args:
        digits (int): How many digits the number should have.

    Returns:
        str: A string of random digits.

    Raises:
        ValueError: If digits is less than 1.
    """
    if digits < 1:
        raise ValueError("digits must be at least 1")

    if digits == 1:
        return str(random.randint(0, 9))

    result = str(random.randint(1, 9))
    for i in range(digits - 1):
        result += str(random.randint(0, 9))

    return result