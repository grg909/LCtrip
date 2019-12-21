# -*- coding: UTF-8 -*-

# @Date    : 2019/12/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# coding style很重要，要写到bug free
# Time O(mn)
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1

        len_h, len_n = len(haystack), len(needle)
        for i in range(len_h - len_n + 1):
            j = 0
            while j < len_n:
                if haystack[i + j] != needle[j]:
                    break
            if j == len_n:
                return i
        return -1
