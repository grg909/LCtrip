# -*- coding: UTF-8 -*-

# @Date    : 2019/12/4
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# O(N)
import unittest


def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [('waterbottle', 'erbottlewat', True), ('foo', 'bar', False),
            ('foo', 'foofoo', False)]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()



"""
Thinking process:
1. if s2 is the rotation of s1, then what is the rotaion point is?
2. we can think of s1 is xy, then s2 is yx
3. see xy always be a substring of yxyx
"""
