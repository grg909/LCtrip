# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):

        lenA, lenB = 0, 0
        node1, node2 = headA, headB
        while node1:
            lenA += 1
            node1 = node1.next
        while node2:
            lenB += 1
            node2 = node2.next

        node1, node2 = headA, headB
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1
        while lenB > lenA:
            node2 = node2.next
            lenB -= 1
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1
