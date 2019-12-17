# -*- coding: UTF-8 -*-

# @Date    : 2019/12/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        # write your code here
        return sorted(chars, key=lambda c: c.isupper())
