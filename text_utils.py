def reverse_string(s):
    """Return the string reversed."""
    return s[::-1]


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print("CI Demo Project (Tanvi)")
    print("Reverse of 'tanvi':", reverse_string("tanvi"))
    print("Is 'Never odd or even' a palindrome:", is_palindrome("Never odd or even"))
