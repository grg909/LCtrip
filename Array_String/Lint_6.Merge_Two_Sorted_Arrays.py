# -*- coding: UTF-8 -*-

# @Date    : 2019/12/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Thinking process:
# 1. 两个指针对数组从小到大遍历，每次取二者较小的放在新数组
# 2. 直到某个数组的指针到结尾，将另一个数组的剩余部分放到新数组中
# Time O(n)
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        result = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        while i < len(A):
            result.append(A[i])
            i += 1
        while j < len(B):
            result.append(B[j])
            j += 1

        return result
