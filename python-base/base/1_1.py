#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/26
# @Author : zengsm
# @File : 1_1 @Description:


def trigon():
    for i in range(0, 11):
        if i == 1:
            print(' ' * 5 + '*')
        elif i % 2 == 1:
            sp = int((12 - i) / 2)
            print(' ' * sp + '*' + ' ' * (i - 2) + '*')
        else:
            print()
    print('* ' * 6)


def sumZero(nums: []):
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
    # trigon()
    # nums = [-3, -1, 0, 1, 2, -4, 6, 7, -8, 9, 15]
    nums = [-1, 0, 1, 2, -4, -3]

    sumZero(nums)
