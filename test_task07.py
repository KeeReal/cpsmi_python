import unittest

from task07 import increase_items_at_main_diag as s


class Task07(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(s(2,
                           [
                               [1, 1],
                               [2, 1]
                           ]), [
                             [2, 1],
                             [2, 2]
                         ])

        self.assertEqual(s(1,
                           [
                               [1],
                           ]), [
                             [2],
                         ])

        self.assertEqual(s(3,
                           [
                               [3, 2, 4],
                               [1, 3, 5],
                               [1, 4, 3]
                           ]), [
                             [4, 2, 4],
                             [1, 5, 5],
                             [1, 4, 6]
                         ])
