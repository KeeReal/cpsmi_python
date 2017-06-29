import unittest

import task02


class Task02(unittest.TestCase):
    def test_shouldReturnMinus1(self):
        items = [2, 6, 2, 2, 1]
        self.assertEqual(task02.sum_between_min_max(items), -1)

    def test_shouldReturnExpectedResult(self):
        items = [4, 3, 2, 1, 2, 3, 4, 5, 6, 1]
        expected = 1 + 2 + 3 + 4 + 5 + 6
        self.assertEqual(task02.sum_between_min_max(items), expected)
