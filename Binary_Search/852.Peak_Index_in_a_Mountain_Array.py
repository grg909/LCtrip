# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:

        if not A:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid - 1] > A[mid]:
                end = mid
            if A[mid - 1] < A[mid]:
                start = mid

        return start if A[start] > A[end] else end
