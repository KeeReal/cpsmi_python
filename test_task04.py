import unittest

import task04


class Task04(unittest.TestCase):
    def test_shouldReturnZero(self):
        self.assertEqual(task04.num_negatives_between_two_first_zeroes([]), -1)
        self.assertEqual(task04.num_negatives_between_two_first_zeroes([0]), -1)

    # def test_shouldReturnExpectedResult(self):
