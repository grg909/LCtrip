# -*- coding: UTF-8 -*-

# @Date    : 2019/12/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# O(n)

# 从例子可以看出，不需要考虑空格，书中给出的答案也不考虑其他特殊符号

import unittest
from collections import Counter


def isPermutationOfPalindrome(string):
    counter = Counter(string.lower())
    oddCount = 0
    for c in counter:
        if not c.isalnum():
            continue
        if counter[c] % 2 == 1:
            oddCount += 1
        if oddCount > 1:
            return False
    return True

class Test(unittest.TestCase):
    dataT = ['abz zab', 'Tact']