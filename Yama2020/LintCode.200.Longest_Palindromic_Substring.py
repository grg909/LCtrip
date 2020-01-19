# -*- coding: UTF-8 -*-

# @Date    : 2020/1/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： 基于中心点枚举的算法，时间复杂度 O(n^2)
    注意：palindromic奇和偶数个的两种情况
"""


class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ""

        start, longest = 0, 0
        for i in range(len(s)):
            length = self.findLongestPalindromeFrom(s, i, i)
            if length > longest:
                longest = length
                start = i - length // 2

            length = self.findLongestPalindromeFrom(s, i, i + 1)
            if length > longest:
                longest = length
                start = i - length // 2 + 1

        return s[start:start + longest]

    def findLongestPalindromeFrom(self, s, left, right):
        length = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            length += 1 if left == right else 2
            left, right = left - 1, right + 1
        return length
