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
        """Set up the ScoreTracker with a file to save scores to."""
        self.filepath = filepath

    def get_high_score(self):
        """
        Read the high score from the file.
        Returns 0 if the file doesn't exist yet or can't be read.
        Returns:
            int: The stored high score, or 0 if there isn't one yet.
        """
        if not os.path.exists(self.filepath): # first check if file exists 
            return 0 # score is 0 if file doesn't exist
        try: 
            file = open (self.filepath, "r") # opens file in order to read
            score = int(file.read().strip()) # reads number inside and converts 
            file.close
            return score 
        except:
            return 0 # return 0 if something goes wrong 


    def save_score(self, score):
        """
        Save the score if it's higher than the current high score.

        Args:
            score (int): The player's score from this session.
        """
        if score > self.get_high_score(): # save only if its a new high score 
            file = open(self.filepath, "w") # open file to write to it 
            file.write(str(score)) # write score as a string into the file 
            file.close
            print("New high score saved!")