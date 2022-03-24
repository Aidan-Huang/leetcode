from typing import List


# 两数之和
def test0001():
    def two_sum(nums, target):
        pass

    nums = [2, 7, 11, 15];
    target = 9
    assert two_sum(nums, target) == [0, 1]

    nums = [3, 2, 4];
    target = 6
    assert two_sum(nums, target) == [1, 2]

    nums = [3, 3];
    target = 6
    assert two_sum(nums, target) == [0, 1]


#   两数相加
def test0002():
    def add_two_numbers(l1, l2):
        pass

    l1 = [2, 4, 3];
    l2 = [5, 6, 4]
    assert add_two_numbers(l1, l2) == [7, 0, 8]
    # 解释：342 + 465 = 807

    l1 = [0];
    l2 = [0]
    assert add_two_numbers(l1, l2) == [0]

    l1 = [9, 9, 9, 9, 9, 9, 9];
    l2 = [9, 9, 9, 9]
    assert add_two_numbers(l1, l2) == [8, 9, 9, 9, 0, 0, 0, 1]

