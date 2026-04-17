"""
test_memory_master.py - Unit tests for MemoryMaster.
"""

import unittest
from number_generator import generate_number


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


# rest of tests still need to be written

class TestWordGenerator(unittest.TestCase):
    def test_correct_count(self):
        pass
    def test_correct_answer(self):
        pass


class TestPatternGenerator(unittest.TestCase):
    def test_correct_rows_and_cols(self):
        pass
    def test_correct_pattern_answer(self):
        pass


class TestScoreTracker(unittest.TestCase):
    def test_starts_at_zero(self):
        pass
    def test_saves_high_score(self):
        pass


class TestGame(unittest.TestCase):
    def test_starts_at_level_1(self):
        pass
    def test_advance_level(self):
        pass


if __name__ == "__main__":
    unittest.main()