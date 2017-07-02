import unittest

import task15


class Task15(unittest.TestCase):
    def test_shouldReturnExpectedResult_False(self):
        self.assertEqual(task15.contains(3, range(10, 0, -2)), False)
        self.assertEqual(task15.contains(3, []), False)
        self.assertEqual(task15.contains(3, [2, 1]), False)
        self.assertEqual(task15.contains(0, [2, 1]), False)

    def test_shouldReturnExpectedResult_True(self):
        self.assertEqual(task15.contains(2, range(10, 0, -1)), True)
        self.assertEqual(task15.contains(10, range(10, 0, -1)), True)
        self.assertEqual(task15.contains(1, range(10, 0, -1)), True)
