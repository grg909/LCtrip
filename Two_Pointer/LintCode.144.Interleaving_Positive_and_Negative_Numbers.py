# -*- coding: UTF-8 -*-

# @Date    : 2019/12/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 先partition，再交换。Time O(n)
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # write your code here
        self.partition(A)
        left, right = 0, len(A) - 1
        while left <= right:
            if not left % 2 and A[left] < 0 and A[right] > 0:
                A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

        return A

    def partition(self, A):
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
