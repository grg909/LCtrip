# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# 另方法一，遍历比较


# O(logn)
class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        start, end = 0, len(letters) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if letters[mid] > target:
                end = mid
            if letters[mid] < target:
                start = mid
            if letters[mid] == target:
                start = mid

        if letters[start] > target:
            return letters[start]
        if letters[end] > target:
            return letters[end]
