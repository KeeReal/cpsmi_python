import unittest

import p2_task1_1


class Part2Task11(unittest.TestCase):
    def test_shouldShuffleWord(self):
        self.assertEqual(p2_task1_1.shuffle_word("Hello", 12), "Hlleo")
        self.assertEqual(p2_task1_1.shuffle_word("a"), "a")
        self.assertEqual(p2_task1_1.shuffle_word("ab"), "ab")
        self.assertEqual(p2_task1_1.shuffle_word("abc"), "abc")

    def test_shouldShuffleText(self):
        text = 'Dear president Blatter, colleagues of the executive committee.'
        expected = 'Dear pideresnt Bttaler, cegaolules of the eutixecve cittommee.'
        self.assertEqual(p2_task1_1.shuffle_text(text, 12), expected)
