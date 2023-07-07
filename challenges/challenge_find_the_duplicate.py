import collections


def find_duplicate(nums):
    if not nums:
        return False
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
    duplicate_dict = collections.Counter(nums)
    sorted_dict = sorted(
        duplicate_dict.items(), key=lambda items: items[1], reverse=True
    )
    if sorted_dict[0][1] == 1:
        return False
    return sorted_dict[0][0]
