import unittest

import task_levenshein as lev


class Task2Levenshtein(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(lev.levenshtein_dist("Hello", 5, "Hell", 4), 1)
        self.assertEqual(lev.levenshtein_dist("abc", 3, "cba", 3), 2)
        self.assertEqual(lev.levenshtein_dist("ah", 2, "text", 4), 4)
