def is_palindrome_iterative(word):
    if not word:
        return False
    return list(word) == list(reversed(word))
