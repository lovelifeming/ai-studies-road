#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/26
# @Author : zengsm
# @File : 1_1 @Description:


def trigon(start, end):
    # 打印倒 * 三角
    for i in range(start, end):
        if i == 1:
            print(' ' * (end//2-1) + '*')
        elif i % 2 == 1:
            sp = int((end - i) / 2)
            print(' ' * sp + '*' + ' ' * (i - 2) + '*')
        else:
            print()
    print('* ' * (end//2))


def sumZero(nums: []):
    # 寻找数组中和为 0 的子串
    sorted(nums)
    res = []
    tmp = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            k = 0 - (nums[i] + nums[j])
            if k in nums and nums.index(k) > j and k not in tmp:
                tmp.append(k), tmp.append(nums[i]), tmp.append(nums[j])
                res.append([nums[i], nums[j], k])
                continue
    print(res)


if __name__ == '__main__':
    # trigon(0, 30)
    # nums = [-3, -1, 0, 1, 2, -4, 6, 7, -8, 9, 15]
    nums = [-1, 0, 1, 2, -4, -3]

    sumZero(nums)
