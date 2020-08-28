# -*- coding: UTF-8 -*-

# @Date    : 2020/1/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：https://www.1point3acres.com/bbs/thread-561317-1-1.html
    由于要求的N或者A可能比较大，所以位运算是最高效的算法
    位操作技巧：
    1. 用1<<num把原来的数字的值算出来
    2. 求数字的二进制表示中有多少个1：如果把一个整数减去1，再和原整数做与运算，
    会把该整数最右边一个1变成0。如二进制1100，减去1后变为1011，1100和1011做
    位与运算是1000，把1100最右边的1变成了0
"""


class Solution1:

    def find_shortest(self, A):

        binarian = 0
        for num in A:
            binarian += 1 << num

        count = 0
        while binarian:
            binarian = binarian & (binarian - 1)
            count += 1

        return count


if __name__ == '__main__':
    a = Solution1()
    print(a.find_shortest([1, 0, 2, 0, 0, 2]))
