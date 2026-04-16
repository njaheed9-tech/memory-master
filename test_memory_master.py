"""
test_memory_master.py - Unit tests for MemoryMaster.

Tests the main functions in each module to make sure they work
correctly. Right now only the number generator tests are passing
since that's the only module implemented so far.

Functions that involve printing or user input can't be automatically
tested - see TESTING.md for those.
"""

import os
import unittest
import tempfile

from number_generator import generate_number


# Tests for number_generator.py

class TestNumberGenerator(unittest.TestCase):

    def test_correct_length(self):
        # The number should have exactly as many digits as we asked for
        for digits in range(1, 8):
            result = generate_number(digits)
            self.assertEqual(len(result), digits)

    def test_returns_string(self):
        # Should return a string, not an int
        self.assertIsInstance(generate_number(3), str)

    def test_no_leading_zero(self):
        # Multi-digit numbers should never start with 0
        for i in range(30):
            result = generate_number(4)
            self.assertNotEqual(result[0], "0")

    def test_single_digit_valid(self):
        # Single digit should be between 0 and 9
        for i in range(20):
            result = generate_number(1)
            self.assertIn(result, ["0","1","2","3","4","5","6","7","8","9"])

    def test_invalid_input(self):
        # Should raise an error if digits is 0 or less
        with self.assertRaises(ValueError):
            generate_number(0)


# Tests for word_generator.py - planned but not written yet

class TestWordGenerator(unittest.TestCase):

    def test_correct_count(self):
        # Should return the right number of words
        pass

    def test_no_duplicates(self):
        # All words should be unique
        pass

    def test_invalid_count(self):
        # Should raise an error if count is 0
        pass

    def test_correct_answer(self):
        # Player typing the right words in order should return True
        pass

    def test_wrong_order(self):
        # Wrong order should return False
        pass

    def test_case_doesnt_matter(self):
        # Capital letters should still count as correct
        pass

    def test_extra_spaces(self):
        # Extra spaces between words should still be correct
        pass


# Tests for pattern_generator.py - planned but not written yet

class TestPatternGenerator(unittest.TestCase):

    def test_correct_rows_and_cols(self):
        # Pattern should have the right number of rows and columns
        pass

    def test_returns_list(self):
        # generate_pattern should return a list
        pass

    def test_invalid_size(self):
        # Rows or cols of 0 should raise an error
        pass

    def test_format_adds_spaces(self):
        # format_pattern should add spaces between each character
        pass

    def test_correct_pattern_answer(self):
        # Typing the pattern exactly right should return True
        pass

    def test_wrong_pattern_answer(self):
        # Wrong characters should return False
        pass

    def test_level_1_size(self):
        # Level 1 should give a 1x2 grid
        pass

    def test_level_4_adds_row(self):
        # Level 4 should have more than 1 row
        pass

    def test_invalid_level(self):
        # Level 0 should raise an error
        pass


# Tests for score_tracker.py - planned but not written yet

class TestScoreTracker(unittest.TestCase):

    def test_starts_at_zero(self):
        # Should return 0 when there's no file yet
        pass

    def test_saves_high_score(self):
        # Saving a score should store it correctly
        pass

    def test_lower_score_not_saved(self):
        # A lower score shouldn't overwrite a higher one
        pass

    def test_higher_score_replaces_old(self):
        # A new high score should replace the old one
        pass


# Tests for game.py - planned but not written yet

class TestGame(unittest.TestCase):

    def test_starts_at_level_1(self):
        pass

    def test_starts_at_score_0(self):
        pass

    def test_bad_mode_raises_error(self):
        pass

    def test_bad_difficulty_raises_error(self):
        pass

    def test_display_time_easy(self):
        pass

    def test_display_time_medium(self):
        pass

    def test_display_time_hard(self):
        pass

    def test_check_answer_numbers_right(self):
        pass

    def test_check_answer_numbers_wrong(self):
        pass

    def test_advance_level(self):
        pass

    def test_hard_gives_more_points(self):
        pass


if __name__ == "__main__":
    unittest.main()