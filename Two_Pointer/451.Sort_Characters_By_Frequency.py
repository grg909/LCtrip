# -*- coding: UTF-8 -*-

# @Date    : 2019/12/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import Counter


# 计数排序，use hashtable, Time O(n), space O(n)
class Solution1:

    def frequencySort(self, s: str) -> str:

        counter = Counter(s)
        result = counter.most_common()

        index = 0
        res = ''
        for char, fre in result:
            while fre:
                res += char
                index += 1
                fre -= 1

        return res


# 更pythonic的写法， 学习了
class Solution2:

    def frequencySort(self, s: str) -> str:

        counter = Counter(s)
        result = counter.most_common()

        index = 0
        res = ''
        for char, fre in result:
            res += char * fre

        return res
