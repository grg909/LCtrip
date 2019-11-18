# -*- coding: UTF-8 -*-

# @Date    : 2019/11/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 比较类似340那道题，同样用字典记录字符出现次数，然后用子序列中出现频率最大的次数加上能被修改的次数K 和窗口长度相比（也就是说窗口中都能统一）

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        tmp = 0
        res = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1
            tmp = max(tmp, char_dict[s[i]])
            if tmp + k < i - start + 1:
                char_dict[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res
