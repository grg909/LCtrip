# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid - 1] > A[mid]:
                end = mid
            if A[mid - 1] < A[mid]:
                start = mid

        if A[start - 1] < A[start] and A[start + 1] < A[start]:
            return start
        if A[end - 1] < A[end] and A[end + 1] < A[end]:
            return end
