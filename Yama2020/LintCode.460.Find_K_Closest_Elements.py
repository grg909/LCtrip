# -*- coding: UTF-8 -*-

# @Date    : 2020/1/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution1:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        index = self.first_index(A, target)
        left, right = index, index + 1
        result = []
        for i in range(k):
            if left == -1:
                result.append(A[right])
                right += 1
            elif right == len(A):
                result.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1

        return result

    def first_index(self, A, target):
        # find the last number <= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[end] <= target:
            return end
        if A[start] <= target:
            return start

        return -1


class Solution2:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        index = self.find_upper_closest(A, target)
        left, right = index - 1, index

        result = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1

    def find_upper_closest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end

        return end + 1

    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
