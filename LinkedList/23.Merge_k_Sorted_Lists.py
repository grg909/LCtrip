# -*- coding: UTF-8 -*-

# @Date    : 2020/3/10
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

ListNode.__lt__ = lambda x, y: (x.val < y.val)


# Use heap
class Solution1:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        dummy = ListNode(-1)
        tail = dummy
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            head = heapq.heappop(heap)
            tail.next = head
            tail = head
            if head.next:
                heapq.heappush(heap, head.next)

        return dummy.next


class Solution2:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_list(left, right)

    def merge_two_list(self, head1, head2):
        cur = dummy = ListNode(-1)

        while head1 and head2:
            if head2.val > head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head2
            cur = cur.next

        if head1:
            cur.next = head1
        if head2:
            cur.next = head2

        return dummy.next
