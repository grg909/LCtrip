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
        if size < 3:
            return 0

        dp = [0 for i in range(size)]
        for i in range(2, size):
            if (A[i] - A[i - 1]) == (A[i - 1] - A[i - 2]):
                dp[i] = dp[i - 1] + 1

        return sum(dp)


if __name__ == '__main__':
    a = Solution()
    print(a.numberOfArithmeticSlices([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
