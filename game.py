"""
game.py - Main game logic for MemoryMaster.

This file contains the MemoryMasterGame class that runs the game.
It handles level progression, checking answers, and keeping score
for all three game modes: numbers, phrases, and pictures.
"""

import os
import time

from number_generator import generate_number
from word_generator import generate_word_list, check_word_list_answer
from pattern_generator import generate_pattern, format_pattern, check_pattern_answer, get_pattern_size
from score_tracker import ScoreTracker


class MemoryMasterGame:
    """
    The main game class for MemoryMaster.

    Keeps track of the level, score, mode, and difficulty.
    Handles showing challenges, getting player input, and
    checking if the answer is right.

    Attributes:
        mode (str): Which game mode is being played (numbers, phrases, or pictures).
        difficulty (str): How hard the game is (easy, medium, or hard).
        level (int): What level the player is on.
        score (int): The player's current score.
        score_tracker (ScoreTracker): Used to save and load the high score.
    """

    def __init__(self, mode="numbers", difficulty="medium"):
        """
        Set up a new game.

        Args:
            mode (str): Game mode - 'numbers', 'phrases', or 'pictures'.
            difficulty (str): Difficulty - 'easy', 'medium', or 'hard'.

        Raises:
            ValueError: If mode or difficulty is not a valid option.
        """
        pass

    def get_display_time(self):
        """
        Get how many seconds to show the challenge based on difficulty.

        Returns:
            float: Number of seconds to display the challenge.
        """
        pass

    def generate_challenge(self):
        """
        Create a new challenge for the current level and mode.

        Returns:
            str or list: A number string, list of words, or list of
            pattern rows depending on the mode.
        """
        pass

    def check_answer(self, challenge, player_answer):
        """
        Check if the player's answer is correct.

        Args:
            challenge (str or list): The original challenge that was shown.
            player_answer (str): What the player typed in.

        Returns:
            bool: True if the answer is correct, False if not.
        """
        pass

    def get_points(self):
        """
        Calculate how many points the player earns for this level.

        Points are based on the current level and difficulty.
        Harder difficulty gives more points.

        Returns:
            int: Points to add to the score.
        """
        pass

    def advance_level(self):
        """Add points to the score and go to the next level."""
        pass

    def format_challenge(self, challenge):
        """
        Convert a challenge into a string that can be printed.

        Args:
            challenge (str or list): The challenge to format.

        Returns:
            str: A printable version of the challenge.
        """
        pass

    def show_challenge(self, challenge):
        """
        Print the challenge on screen, wait, then clear the screen.

        Args:
            challenge (str or list): The challenge to display.
        """
        pass

    def get_player_answer(self):
        """
        Ask the player to type their answer and return what they typed.

        For pictures mode, the player types one row at a time and
        presses Enter on a blank line when done.

        Returns:
            str: The player's answer as a string.
        """
        pass

    def run(self):
        """
        Run the game from start to finish.

        Shows the welcome message, loops through levels until
        the player gets one wrong, then shows the final score.
        """
        pass


def clear_screen():
    """Clear the terminal so the player can't scroll back and see the answer."""
    pass


def print_welcome(mode, difficulty):
    """
    Print a welcome message at the start of the game.

    Args:
        mode (str): The game mode the player chose.
        difficulty (str): The difficulty the player chose.
    """
    pass
