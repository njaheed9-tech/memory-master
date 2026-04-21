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
        if self.mode == "numbers":
            return generate_number(self.level) # generates a number with as many digits as the current level 
        elif self.mode == "phrases": 
            return generate_word_list(self.level + 1) # generates word list, +1 to start with 2 words 
        else: 
            rows, cols = get_pattern_size(self.level) # figures out how big the grid should be 
            return generate_pattern(rows, cols) # generates pattern with those dimensions 

    def check_answer(self, challenge, player_answer):
        """Return True if the player's answer is correct, False if not."""
        if self.mode == "numbers":
            return player_answer.strip() == challenge # removes any extra spaces, then check if matches number
        elif self.mode == "phrases":
            return check_word_list_answer(challenge, player_answer) # uses word_generator's checker
        else:
            return check_pattern_answer(challenge, player_answer) # uses pattern_generator's checker

    def get_points(self):
        """Calculate points earned for the current level."""
        if self.difficulty == "easy":
            multiplier = 1 
        elif self.difficulty == "medium":
            multiplier = 2
        else: 
            multiplier = 3 
        return self.level * 10 * multiplier # higher level and harder difficulty = morep oints 

    def advance_level(self):
        """Add points to the score and move to the next level."""
        self.score += self.get_points() # add points to the score 
        score += 1 # go to next level 

    def show_challenge(self, challenge):
        """Print the challenge, wait, then clear the screen."""
        if self.mode == "numbers":
            print(f"\n{challenge}\n") # prints number 
        elif self.mode == "phrases":
            print(f"\n{'  '.join(challenge)}\n") # prints words and separates by spaces
        else: 
            for row in challenge: 
                print(" ".join(row)) # prints each row of the pattern with spaces between characters
        time.sleep(self.get_display_time()) # waits based off difficulty 
        clear_screen() # so player cant see 


    def get_player_answer(self):
        """Ask the player for their answer and return what they typed."""
        if self.mode == "numbers":
            return input("Type the number you saw: ")
        elif self.mode == "phrases":
            return input("Type the words in order (separated by spaces): ")
        else:
            print("Type the pattern row by row. Press Enter on a blank line when done.")
            lines = []
            while True:
                line = input()
                if line == "": # blank line = player is done 
                    break
                lines.append(line)
                return "\n".join(lines) # joins all the rows into one string 

    def run(self):
        """Run the game loop until the player gets one wrong."""
        print_welcome(self.mode, self.difficulty) # welcome message 

        while True:
            challenge = self.generate_challenge() # creates new challenge for this level

            print(f"Level: {self.level} | Score: {self.score}")
            print(f"Memorize this: ")
            time.sleep(1)

            self.show_challenge(challenge) # shows challenge, clears screen 

            player_answer = self.get_player_answer() # asks player for their answer 

            if self.check_answer(challenge, player_answer):
                print("Correct")
                self.advance_level()
            else: 
                print("Wrong! The correct answer was:")
                print(f"Game over. Final score: {self.score}")

                self.score_tracker.save_score(self.score) # save score 
                high = self.score_tracker.get_high_score() # gets high score 
                print(f"High score for {self.mode} mode: {high}")

                break 


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_welcome(mode, difficulty):
    """Print a welcome message with the mode and difficulty."""
    print("Welcome to MemoryMaster!")
    print(f"Mode: {mode.capitalize()}")
    print(f"Difficulty: {difficulty.capitalize()}")