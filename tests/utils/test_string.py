from utils.string import is_palindrome


def test_is_palindrome() -> None:
    assert is_palindrome("")
    assert is_palindrome(" ")
    assert is_palindrome("racecar")
    assert not is_palindrome("ab")
    assert not is_palindrome("racecarr")
