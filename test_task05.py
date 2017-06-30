import unittest

import task05


class Task04(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(task05.del_all_zeroes_after_max_item([]), [])
        self.assertEqual(task05.del_all_zeroes_after_max_item([0,1]), [0,1])
        self.assertEqual(task05.del_all_zeroes_after_max_item([1,0,2,0]), [1,0,2])
        self.assertEqual(task05.del_all_zeroes_after_max_item([0,0,0]), [0])
        self.assertEqual(task05.del_all_zeroes_after_max_item([2,0,0,0,0]), [2])
