"""
number_generator.py - Generates random numbers for MemoryMaster.

This module handles creating random numbers of different lengths
depending on what level the player is on.
"""

import random


def generate_number(digits, add_commas=False, allow_leading_zero=False):
    """
    Generate a random number string with a given number of digits.

    The first digit will never be 0 so the number always has
    the right amount of digits.

    Args:
        digits (int): How many digits the number should have.
        add_commas (bool): If True, add commas as thousands separators.
        allow_leading_zero (bool): If True, first digit can be 0 (harder).

    Returns:
        str: A string of random digits.

    Raises:
        ValueError: If digits is less than 1.
    """
    if digits < 1:
        raise ValueError("digits must be at least 1")

    if digits == 1:
        if allow_leading_zero:
            number = str(random.randint(0, 9))
        else:
            number = str(random.randint(0, 9))
    else:
        # Generate first digit
        if allow_leading_zero:
            first_digit = str(random.randint(0, 9))
        else:
            first_digit = str(random.randint(1, 9))
        
        # Generate remaining digits
        remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(digits - 1))
        number = first_digit + remaining_digits
    
    # Add commas as thousands separators if requested
    if add_commas and digits > 3:
        # Convert to int, add commas, convert back to string
        try:
            number_int = int(number)
            number = f"{number_int:,}"
        except ValueError:
            # If number has leading zeros, int() will remove them
            # Keep original format for leading zero case
            pass
    
    return number


def generate_number_with_leading_zero(digits):
    """
    Generate a random number where the first digit CAN be zero.
    This is harder for players to remember.

    Args:
        digits (int): How many digits the number should have.

    Returns:
        str: A string of random digits (may start with 0).
    """
    if digits < 1:
        raise ValueError("digits must be at least 1")
    
    return ''.join(str(random.randint(0, 9)) for _ in range(digits))


def get_number_difficulty_level(digits):
    """
    Return a difficulty rating for a number based on its length.

    Args:
        digits (int): Number of digits.

    Returns:
        str: 'easy', 'medium', or 'hard'
    """
    if digits <= 3:
        return "easy"
    elif digits <= 6:
        return "medium"
    else:
        return "hard"