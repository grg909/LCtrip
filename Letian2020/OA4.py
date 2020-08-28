# -*- coding: UTF-8 -*-

# @Date    : 2020/2/7
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    给定一个数组a，ai = (-2)^i（就是代表一个负二进制的数），问这个数组代表的数字除以二向上取整的结果如何用最短的负二进制来表示。
    解题报告：位运算结果向下取整
    所以对于正数来说位运算和除法结果是一样的，因为正数的向下取整也就是向0取整；而对于负数来说，向下取整要比向0取整小1.
"""


class Solution1:

    def find_shortest(self, A):

        binarian = 0
        for num in A:
            binarian += (-2)**num

        N = binarian >> 1 + 1
        count = 0
        while N:
            r = N % (-2)
            N //= (-2)
            if r < 0:
                N += 1
            count += 1

        return count


if __name__ == '__main__':
    a = Solution1()
    print(a.find_shortest([1, 0, 2, 0, 0, 2]))
