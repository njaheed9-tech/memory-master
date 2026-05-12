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

    # More efficient: generate first digit (1-9) then remaining digits (0-9)
    first_digit = str(random.randint(1, 9))
    remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(digits - 1))
    
    return first_digit + remaining_digits