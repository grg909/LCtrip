# -*- coding: UTF-8 -*-

# @Date    : 2020/1/8
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
    @param head: The head of linked list.
    @return: nothing
    """

    def reorderList(self, head):
        if not head or not head.next:
            return

        mid = self.find_middle(head)
        tail = self.reverse(mid.next)
        mid.next = None

        self.merge(head, tail)

    def find_middle(self, head):
        # 1(head) -> 2 -> 3 -> 4
        slow, fast = head, head.next
        # 由于奇和偶两种情况
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge(self, head1, head2):
        # 1(head1) -> 2
        # 4(head2) -> 3
        dummy = ListNode(-1)
        index = 0

        while head1 and head2:
            if index % 2 == 0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index += 1
        if head1:
            dummy.next = head1
        else:
            dummy.next = head2
