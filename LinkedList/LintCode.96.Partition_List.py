# -*- coding: UTF-8 -*-

# @Date    : 2020/1/7
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：双dummy加双指针
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # 1 -> 4 -> 2 -> [3] -> 5
        # a_head -> 1 -> 2 (a_tail)
        # b_head -> [3] -> 4 -> 5 (b_tail)
        if not head:
            return head

        a_head, b_head = ListNode(-1), ListNode(-1)
        a_tail, b_tail = a_head, b_head
        while head:
            if head.val < x:
                a_tail.next = head
                a_tail = a_tail.next
            else:
                b_tail.next = head
                b_tail = b_tail.next
            head = head.next
        b_tail.next = None
        a_tail.next = b_head.next
        return a_head.next