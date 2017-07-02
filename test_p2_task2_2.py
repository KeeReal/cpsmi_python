import unittest

import p2_task2_2


class Part2Task11(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(p2_task2_2.levenshtein_dist("Hello", 5, "Hell", 4), 1)
        self.assertEqual(p2_task2_2.levenshtein_dist("abc", 3, "cba", 3), 2)
        self.assertEqual(p2_task2_2.levenshtein_dist("ah", 2, "text", 4), 4)
