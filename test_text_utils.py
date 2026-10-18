import unittest
from text_utils import reverse_string, is_palindrome


class TestTextUtils(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_string("tanvi"), "ivnat")

    def test_reverse_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("Never odd or even"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("tanvi"))


if __name__ == "__main__":
    unittest.main()
