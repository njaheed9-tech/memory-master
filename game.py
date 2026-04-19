"""
game.py - Main game logic for MemoryMaster.
"""

import os
import time

from number_generator import generate_number
from word_generator import generate_word_list, check_word_list_answer
from pattern_generator import generate_pattern, format_pattern, check_pattern_answer, get_pattern_size
from score_tracker import ScoreTracker


class MemoryMasterGame:
    """
    Main game class. Keeps track of level, score, mode, and difficulty.
    """

    def __init__(self, mode="numbers", difficulty="medium"):
        """Set up a new game with the given mode and difficulty."""
        valid_modes = ["numbers", "phrases", "pictures"]
        valid_difficulties = ["easy", "medium", "hard"]

        if mode not in valid_modes:
            raise ValueError("Mode must be in numbers, phrases, or pictures")
        if difficulty not in valid_difficulties:
            raise ValueError("Difficulty must be easy, medium, or hard")
        
        self.mode = mode 
        self.diffculty = difficulty 
        self.level = 1 
        self.score = 0 
        self.score_tracker = ScoreTracker(filepath=f"High_score_{mode}.txt")

    def get_display_time(self):
        """Return how many seconds to show the challenge."""
        if self.difficulty == "easy":
            return 5.0 
        elif self.difficulty == "medium":
            return 3.0 
        else: 
            return 1.5

    def generate_challenge(self):
        """Create a challenge for the current level and mode."""
        pass

    def check_answer(self, challenge, player_answer):
        """Return True if the player's answer is correct, False if not."""
        pass

    def get_points(self):
        """Calculate points earned for the current level."""
        pass

    def advance_level(self):
        """Add points to the score and move to the next level."""
        pass

    def show_challenge(self, challenge):
        """Print the challenge, wait, then clear the screen."""
        pass

    def get_player_answer(self):
        """Ask the player for their answer and return what they typed."""
        pass

    def run(self):
        """Run the game loop until the player gets one wrong."""
        pass


def clear_screen():
    """Clear the terminal screen."""
    pass


def print_welcome(mode, difficulty):
    """Print a welcome message with the mode and difficulty."""
    pass