from typing import List


# 两数之和
# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
def test0001():
    # Eric 2022-03-25
    def two_sum(nums, target):
        return aidan220325(nums, target)
        # return eric220325(nums, target)

    def aidan220325(nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def eric220325(nums, target):
        index = 0
        # 依次选取数组中的数子，并依次与所有后面的数字相加，判断和是否为8
        while index < len(nums) - 1:
            for n in range(1, len(nums) - index):
                if nums[index] + nums[index + n] == target:
                    return [index, index + n]
            index += 1
        return []

    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]


#   两数相加
def test0002():
    def add_two_numbers(l1, l2):
        short = l1
        long = l2

        if len(l1) > len(l2):
            short = l2
            long = l1

        up = 0

        result = []

        for i in range(len(short)):
            single_sum = short[i] + long[i] + up
            result.append(single_sum % 10)
            up = int(single_sum / 10)

        for j in range(len(short), len(long)):
            single_sum = long[j] + up
            result.append(single_sum % 10)
            up = int(single_sum / 10)

        if up > 0:
            result.append(up)

        return result


    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    assert add_two_numbers(l1, l2) == [7, 0, 8]
    # 解释：342 + 465 = 807

    l1 = [0]
    l2 = [0]
    assert add_two_numbers(l1, l2) == [0]

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    assert add_two_numbers(l1, l2) == [8, 9, 9, 9, 0, 0, 0, 1]


# 无重复字符的最长子串
# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
def test0003():
    def length_of_longest_substring(s):
        return eric220326(s)

    def eric220326(s):
        pass

    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3  # "abc"

    s = "bbbbb"
    assert length_of_longest_substring(s) == 1

    s = "pwwkew"
    assert length_of_longest_substring(s) == 3
