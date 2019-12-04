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


def is_permutation_palindrome(string):
    """
    another implementation
    :param string:
    :return:
    """
    counter = Counter(string.lower())
    countodd = 0
    for c in counter:
        if not c.isalnum():
            continue
        if counter[c] % 2 == 1:
            countodd += 1
        if countodd > 1:
            return False
    return True


def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


def pal_per(phrase):
    """'function checks if a string is a permutation of a palindrome or not"""
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1
    return countodd <= 1


class Test(unittest.TestCase):
    data = [('Tact Coa', True), ('jhsabckuj ahjsbckj', True),
            ('Able was I ere I saw Elba', True),
            ('So patient a nurse to nurse a patient so', False),
            ('Random Words', False), ('Not a Palindrome', False),
            ('no x in nixon', True), ('azAZ', True)]

    def test_pal_perm(self):
        for test_string, expected in self.data:
            actual = pal_per(test_string)
            self.assertEqual(actual, expected)

    def test_is_permutation_palindrome(self):
        for test_string, expected in self.data:
            actual = is_permutation_palindrome(test_string)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
