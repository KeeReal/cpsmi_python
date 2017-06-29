import unittest

import task01


class Task01(unittest.TestCase):
    def test_shouldReverseString(self):
        self.assertEqual(task01.reverse_string('hello world!'), '!dlrow olleh')
