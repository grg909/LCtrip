# -*- coding: UTF-8 -*-

# @Date    : 2019/12/13
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Given a sorted array of distinct int, write a function that return
# the lowest index i for which arr[i] == i, return -1 if there is no
# such index


class Solution:

    def indexEquaalsValueSearch(self, nums) -> int:

        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > mid:
                end = mid
            if nums[mid] < mid:
                start = mid
            if nums[mid] == mid:
                end = mid

        if nums[start] == start:
            return start
        elif nums[end] == end:
            return end

        return -1


if __name__ == '__main__':
    a = Solution()
    print(a.indexEquaalsValueSearch([-8, 0, 2, 5]))
    print(a.indexEquaalsValueSearch([-1, 0, 3, 6]))
    print(a.indexEquaalsValueSearch([-1, 1, 2, 6]))


# follow up: what about there is duplication inside the sorted array?