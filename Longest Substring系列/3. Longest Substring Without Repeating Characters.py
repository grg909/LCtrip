# -*- coding: UTF-8 -*-

# @Date    : 2019/11/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 这道题就是使用一个dict来维护字符出现的位置，一旦发现新字符出现在字典里并且start的位置 <= 记录位置（就是连续同样字符保留最后一个）
# start更新为上个出现该字符的index+1，类似滑动窗口，一旦发现重复元素就去把上一次的元素位置+1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            dic[s[i]] = i
        return res
