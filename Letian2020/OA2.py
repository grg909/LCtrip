# -*- coding: UTF-8 -*-

# @Date    : 2020/1/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：https://www.1point3acres.com/bbs/thread-564350-1-1.html
    LintCode.982
"""


class Solution:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """

    def numberOfArithmeticSlices(self, A: list) -> int:
        size = len(A)
        if size in (0, 1, 2):
            return 0

        t = [A[i] - A[i - 1] for i in range(1, size)]
        dp = [0 for i in range(size)]
        for i in range(2, size):
            if t[i - 2] == t[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0

        return sum(dp)


if __name__ == '__main__':
    a = Solution()
    a.numberOfArithmeticSlices([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0])
