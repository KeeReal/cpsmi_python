import unittest

import task03


class Task03(unittest.TestCase):
    def test_shouldReturnZero(self):
        self.assertEqual(task03.avg_sum_after_last_zero([1,2]), -1)
        self.assertEqual(task03.avg_sum_after_last_zero([]), -1)
        self.assertEqual(task03.avg_sum_after_last_zero([1,0]), -1)

    def test_shouldReturnExpectedResult(self):
        self.assertEqual(task03.avg_sum_after_last_zero([0,1]), 1)
        self.assertEqual(task03.avg_sum_after_last_zero([0,2,2]), 2)
        self.assertEqual(task03.avg_sum_after_last_zero([0,2,0,2,4]), 3)
