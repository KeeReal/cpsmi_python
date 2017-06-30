import unittest

from task10 import num_pairs as s


class Task10(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(s("abc dd cba"), 4)
        self.assertEqual(s("abc d a bcd"), 0)
        self.assertEqual(s("abc         a cba"), 3)
