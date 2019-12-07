# -*- coding: UTF-8 -*-

# @Date    : 2019/12/7
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# • 面试中是否使用 Recursion 的几个判断条件
# 1. 面试官是否要求了不使用 Recursion （如果你不确定，就向面试官询问）
# 2. 不用 Recursion 是否会造成实现变得很复杂
# 3. Recursion 的深度是否会很深
# 4. 题目的考点是 Recursion vs Non-Recursion 还是就是考你是否会Recursion？
# • 记住：不要自己下判断，要跟面试官讨论！


# 注意：以下代码为找last postion（any postion）
class Solution:

    def binary_search(self, array, target):
        if not array:
            return 1

        start, end = 0, len(array) - 1
        # 相邻就退出
        # start = 1 end = 2 就要退出
        while start + 1 < end:
            # python3 默认使用长整型，不用考虑溢出问题
            mid = (start + end) // 2
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid

        # double check
        if array[end] == target:
            return end
        if array[start] == target:
            return start

        return -1


# 若找 first/last, 代码两处不同:1. 32行 2. double check顺序

# python 自带二分库
import bisect

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 5, 5, 5]
    so = Solution()
    print(so.binary_search(a, 5))
