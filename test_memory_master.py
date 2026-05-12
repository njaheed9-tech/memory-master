"""
test_memory_master.py - Unit tests for MemoryMaster.
"""

import unittest
import os
from number_generator import generate_number
from word_generator import generate_word_list, check_word_list_answer
from pattern_generator import get_pattern_size, check_pattern_answer
from score_tracker import ScoreTracker
from game import MemoryMasterGame


class TestNumberGenerator(unittest.TestCase):

    def test_correct_length(self):
        for digits in range(1, 8):
            self.assertEqual(len(generate_number(digits)), digits)

    def test_returns_string(self):
        self.assertIsInstance(generate_number(3), str)

    def test_no_leading_zero(self):
        self.assertNotEqual(generate_number(4)[0], "0")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_number(0)


class TestWordGenerator(unittest.TestCase):
    def test_correct_count(self):
        """Test that generate_word_list returns the correct number of words."""
        for count in range(1, 6):
            words = generate_word_list(count)
            self.assertEqual(len(words), count)
    
    def test_correct_answer(self):
        """Test that check_word_list_answer correctly compares words."""
        target = ["apple", "bridge", "candle"]
        
        # Test correct answer
        self.assertTrue(check_word_list_answer(target, "apple bridge candle"))
        
        # Test wrong order
        self.assertFalse(check_word_list_answer(target, "bridge apple candle"))
        
        # Test wrong words
        self.assertFalse(check_word_list_answer(target, "dog cat mouse"))
        
        # Test case insensitivity
        self.assertTrue(check_word_list_answer(target, "APPLE BRIDGE CANDLE"))


class TestPatternGenerator(unittest.TestCase):
    def test_correct_rows_and_cols(self):
        """Test that get_pattern_size returns a tuple with rows and cols."""
        result = get_pattern_size(1)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
    
    def test_correct_pattern_answer(self):
        """Test that check_pattern_answer correctly compares patterns."""
        target = ["#@", "*+"]
        
        # Test correct answer (player types row by row)
        self.assertTrue(check_pattern_answer(target, "#@\n*+"))
        
        # Test wrong answer
        self.assertFalse(check_pattern_answer(target, "@#\n+*"))
        
        # Test missing row
        self.assertFalse(check_pattern_answer(target, "#@"))


class TestScoreTracker(unittest.TestCase):
    def setUp(self):
        """Create a temporary test file before each test."""
        self.test_file = "test_high_score.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_starts_at_zero(self):
        """Test that get_high_score returns 0 when no file exists."""
        tracker = ScoreTracker(filepath=self.test_file)
        self.assertEqual(tracker.get_high_score(), 0)
    
    def test_saves_high_score(self):
        """Test that save_score only saves if score is higher than current high score."""
        tracker = ScoreTracker(filepath=self.test_file)
        
        # Save first score
        tracker.save_score(100)
        self.assertEqual(tracker.get_high_score(), 100)
        
        # Try to save lower score - should NOT update
        tracker.save_score(50)
        self.assertEqual(tracker.get_high_score(), 100)
        
        # Save higher score - SHOULD update
        tracker.save_score(200)
        self.assertEqual(tracker.get_high_score(), 200)


class TestGame(unittest.TestCase):
    def test_starts_at_level_1(self):
        """Test that a new game starts at level 1."""
        game = MemoryMasterGame(mode="numbers", difficulty="easy")
        self.assertEqual(game.level, 1)
    
    def test_advance_level(self):
        """Test that advance_level increases level by 1 and adds points."""
        game = MemoryMasterGame(mode="numbers", difficulty="easy")
        initial_score = game.score
        initial_level = game.level
        
        game.advance_level()
        
        self.assertEqual(game.level, initial_level + 1)
        self.assertGreater(game.score, initial_score)


if __name__ == "__main__":
    unittest.main()