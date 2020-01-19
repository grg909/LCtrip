# -*- coding: UTF-8 -*-

# @Date    : 2020/1/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：如果TLS，可能算法有问题，也可能是有些特殊情况
    可以简化计算
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
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        # From: 1->[2]->3->[4]->null, v1 = 2, v2 = 4
        # To: 1->[4]->3->[2]->null
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        v1_pre, v2_pre = self.find_node(dummy, v1, v2)
        if not v1_pre or not v2_pre:
            return dummy.next

        # 考虑到相邻情况可以简化计算
        if v1_pre.next == v2_pre:
            self.swapAdjcent(v1_pre)
        elif v2_pre.next == v1_pre:
            self.swapAdjcent(v2_pre)
        else:
            self.swapRemote(v1_pre, v2_pre)

        return dummy.next

    def find_node(self, prev, v1, v2):
        node = prev
        v1_pre, v2_pre = None, None
        while node.next:
            if node.next.val == v1:
                v1_pre = node
            if node.next.val == v2:
                v2_pre = node
            node = node.next
        return v1_pre, v2_pre

    def swapAdjcent(self, pre):
        # dummy -> 1(pre) -> [2] -> [3] -> ...
        node1 = pre.next
        node2 = node1.next

        node1.next = node2.next
        pre.next = node2
        node2.next = node1

    def swapRemote(self, v1_pre, v2_pre):
        # dummy -> 1(v1_pre) -> [2] -> 3(v2_pre) -> [3] -> ...
        node1 = v1_pre.next
        node2 = v2_pre.next

        v1_pre.next = node2
        v2_pre.next = node1
        tmp = node2.next
        node2.next = node1.next
        node1.next = tmp
