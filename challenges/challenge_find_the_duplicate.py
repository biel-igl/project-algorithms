import collections


def find_duplicate(nums):
    if not nums:
        return False
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
    duplicate_dict = collections.Counter(nums)
    most_common = duplicate_dict.most_common(1)
    if most_common[0][1] == 1:
        return False
    return most_common[0][0]
