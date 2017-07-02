import unittest

from task14 import get_all_alphas as s


class Task14(unittest.TestCase):
    def test_shouldReturnExpectedResult(self):
        self.assertEqual(s("Hello 2292 a ---*@&#*"), list("Helloa"))
        # self.assertEqual(s("abc d a bcd"), 0)
        # self.assertEqual(s("abc         a cba"), 3)
