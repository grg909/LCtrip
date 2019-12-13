# -*- coding: UTF-8 -*-

# @Date    : 2019/12/13
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def mySqrt(self, x: int) -> int:

        start, end = 0, x
        while start + 1 < end:
            mid = (start + end)//2
            if mid * mid < x:
                start = mid
            if mid * mid > x:
                end = mid
            if mid * mid == x:
                end = mid

        if end * end == x:
            return end
        if start * start == x:
            return start