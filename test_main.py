import unittest

from main import solve


class SolveTests(unittest.TestCase):
    def test_reverses_words(self):
        self.assertEqual(solve("one two three"), "three two one")

    def test_single_word(self):
        self.assertEqual(solve("hello"), "hello")

    def test_empty_input(self):
        self.assertEqual(solve(""), "")

    def test_normalizes_whitespace(self):
        self.assertEqual(solve("  one\t two\nthree  "), "three two one")

    def test_whitespace_only(self):
        self.assertEqual(solve(" \t\n "), "")


if __name__ == "__main__":
    unittest.main()
