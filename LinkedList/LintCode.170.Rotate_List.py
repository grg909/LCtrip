# -*- coding: UTF-8 -*-

# @Date    : 2020/1/12
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        # dummy -> 1 -> 2 -> 3(tail_pre) -> 4
        # dummy -> 4 -> 1 -> 2(tail_pre) -> 3
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        while k:
            tail_pre = self.find_tail_pre(dummy.next)
            tail = tail_pre.next
            tail_pre.next = None
            tail.next = dummy.next
            dummy.next = tail
            k -= 1

        return dummy.next

    def find_tail_pre(self, head):
        while head.next.next:
            head = head.next
        return head
