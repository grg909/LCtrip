# -*- coding: UTF-8 -*-

# @Date    : 2019/12/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        left, right = 0, len(A)-1
        while left <= right:
            while left <= right and not A[left] %2:
                left += 1
            while left <= right and A[right] % 2:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        return A
