def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    return low_index >= high_index or (
        word[low_index] == word[high_index]
        and is_palindrome_recursive(word, low_index + 1, high_index - 1)
    )
