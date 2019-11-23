# -*- coding: UTF-8 -*-

# @Date    : 2019/11/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 用字典来保存出现次数，用字典的长度维护K值

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_dict = {}
        start = 0
        res = 0

        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1

            while len(char_dict) > k:
                temp = s[start]
                if char_dict[temp] > 1:
                    char_dict[temp] -= 1
                else:
                    del (char_dict[temp])
                start += 1
            res = max(res, i - start + 1)

        return res
