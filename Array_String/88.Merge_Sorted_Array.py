# -*- coding: UTF-8 -*-

# @Date    : 2019/12/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 考点：双指针， coding style
class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        indexA, indexB, insertIndex = m - 1, n - 1, m + n - 1
        while indexA >= 0 and indexB >= 0:
            if nums1[indexA] > nums2[indexB]:
                nums1[insertIndex] = nums1[indexA]
                indexA -= 1
            else:
                nums1[insertIndex] = nums2[indexB]
                indexB -= 1
            insertIndex -= 1

        while indexB >= 0:
            nums1[insertIndex] = nums2[indexB]
            insertIndex -= 1
            indexB -= 1
