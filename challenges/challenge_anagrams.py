def is_anagram(first_string, second_string):
    sorted_first = counting_sort(first_string.lower()) if first_string else ""
    sorted_second = (
        counting_sort(second_string.lower()) if second_string else ""
    )

    if not first_string or not second_string:
        return sorted_first, sorted_second, False

    if len(sorted_first) != len(sorted_second):
        return sorted_first, sorted_second, False

    return sorted_first, sorted_second, sorted_first == sorted_second


def counting_sort(string):
    counts = [0] * 26  # Considerando apenas as letras do alfabeto

    for char in string:
        if "a" <= char <= "z":
            counts[ord(char) - ord("a")] += 1

    sorted_string = []
    for i in range(26):
        sorted_string.extend([chr(i + ord("a"))] * counts[i])

    return "".join(sorted_string)
