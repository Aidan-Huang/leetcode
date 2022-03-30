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
        return eric220328(s)
        # return aidan220326(s)

    def aidan220326(s):
        n = len(s)
        if n <= 1:
            return n
        repeat = []
        n_max = 1
        for i in range(n - n_max):
            repeat.clear()
            repeat.append(s[i])
            for j in range(i + 1, n):
                if s[j] not in repeat:
                    repeat.append(s[j])
                else:
                    break

            if len(repeat) > n_max:
                n_max = len(repeat)

        return n_max

    def eric220328(s):
        t = 0
        if len(s) == 1:
            return 1
        for i in range(0, len(s) - 1):
            s_list = []
            a = 0
            for num in range(i, len(s)):
                is_same = False
                for n in s_list:
                    if s[num] == n:
                        is_same = True
                        if a > t:
                            t = a
                        break
                if not is_same:
                    s_list.append(s[num])
                    a += 1
                else:
                    break
            if a > t:
                t = a
        return t

    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3  # "abc"

    s = "bbbbb"
    assert length_of_longest_substring(s) == 1

    s = "pwwkew"
    assert length_of_longest_substring(s) == 3

    s = ""
    assert length_of_longest_substring(s) == 0

    s = " "
    assert length_of_longest_substring(s) == 1

    s = "au"
    assert length_of_longest_substring(s) == 2

    s = "dvdf"
    assert length_of_longest_substring(s) == 3

    s = "dvdf"
    assert length_of_longest_substring(s) == 3


# 最长回文子串
def test0005():
    def longest_palindrome(s):
        # return eric220330(s)
        return aidan220329(s)

    def aidan220329(s):
        n = len(s)
        n_max = 0
        sub_max = ""
        for i in range(n):
            for j in range(i, n):
                if s[i] == s[j]:
                    sub_s = s[i:j + 1]
                    if sub_s == sub_s[::-1]:
                        if len(sub_s) > n_max:
                            n_max = len(sub_s)
                            sub_max = sub_s

        return sub_max

    def eric220330(s):
        tstring = ""
        n = len(s)
        for i in range(n):
            nstring = ""
            for j in range(i, n):
                nstring += s[j]
                if s[i] == s[j]:
                    if nstring == nstring[::-1]:
                        if len(nstring) > len(tstring):
                            tstring = nstring
        return tstring

    s = "babad"
    assert longest_palindrome(s) == "bab" or longest_palindrome(s) == "aba"

    s = "cbbd"
    assert longest_palindrome(s) == "bb"

# 回文数
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。
def test0009():
    def is_palindrome(x):
        return eric220329(x)

    def eric220329(x):
        l = []
        if x < 0:
            return False
        for char in str(x):
            l.append(char)
        for n in range(0, len(l)):
            if l[-n - 1] != l[n]:
                return False
        return True

    x = 121
    assert is_palindrome(x) is True
    x = -121
    assert is_palindrome(x) is False
    x = 10
    assert is_palindrome(x) is False


# 盛最多水的容器

# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。

# 说明：你不能倾斜容器。
def test0011():
    def max_area(height):
        return eric220331()

    def eric220331(height):
        pass

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(height) == 49

    height = [1, 1]
    assert max_area(height) == 1

