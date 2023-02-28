import palindrome    # The code to test

def test_ispalindrome():
    assert palindrome.is_palindrome("racecar") == True

# This test is designed to fail for demonstration purposes.
def test_isNotPalindrome():
    assert palindrome.is_palindrome(blah) == False