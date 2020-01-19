# -*- coding: UTF-8 -*-

# @Date    : 2020/1/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： 窗口类模板，同向双指针
"""


class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        unique_chars = set()
        j = 0
        size = len(s)
        longest = 0
        for i in range(size):
            while j < size and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])
        return longest
