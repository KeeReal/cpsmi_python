import unittest

from task06 import swap_min_max_cols as s


class Task06(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(s(2, 1,
                           [
                               [1],
                               [2]
                           ]), [
                             [1],
                             [2]
                         ])

        self.assertEqual(s(4, 3,
                           [
                               [1, 1, 2],
                               [1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1],
                           ]), [
                             [2, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1]
                         ])

        self.assertEqual(s(1, 1,
                           [
                               [1]
                           ]), [
                             [1]
                         ])
