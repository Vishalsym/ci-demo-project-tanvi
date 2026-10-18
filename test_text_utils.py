import unittest
from text_utils import reverse_string, is_palindrome, count_vowels


class TestTextUtils(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_string("tanvi"), "tanvi")

    def test_reverse_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("Never odd or even"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("tanvi"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("tanvi"), 2)


if __name__ == "__main__":
    unittest.main()
