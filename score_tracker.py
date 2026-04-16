"""
score_tracker.py - Handles saving and loading the high score for MemoryMaster.

The high score is stored in a simple text file
"""

import os


class ScoreTracker:
    """
    Keeps track of the player's high score using a text file.

    Attributes:
        filepath (str): The path to the file where the high score is saved.
    """

    def __init__(self, filepath="high_score.txt"):
        """
        Set up the ScoreTracker with a file to save scores to.

        Args:
            filepath (str): Path to the high score file.
        """
        pass

    def get_high_score(self):
        """
        Read the high score from the file.

        Returns 0 if the file doesn't exist yet or can't be read.

        Returns:
            int: The stored high score, or 0 if there isn't one yet.
        """
        pass

    def save_score(self, score):
        """
        Save the score if it's higher than the current high score.

        Args:
            score (int): The player's score from this session.
        """
        pass