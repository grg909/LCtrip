# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# Two pointer, O(n)
class Solution1:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return []

        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []


# O(nlogn)
class Solution2:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return []

        end = len(numbers) - 1
        for i, va in enumerate(numbers):
            se = self.search(numbers, target - va, i + 1, end)
            if se != -1:
                return [i, se]

    def search(self, numbers, target, start, end):

        if not numbers:
            return -1

        start, end = start, end
        while start + 1 < end:
            mid = (start + end) // 2
            if numbers[mid] == target:
                start = mid
            if numbers[mid] < target:
                start = mid
            if numbers[mid] > target:
                end = mid

        if numbers[start] == target:
            return start
        if numbers[end] == target:
            return end

        return -1
