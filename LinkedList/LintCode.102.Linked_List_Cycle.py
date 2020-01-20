# -*- coding: UTF-8 -*-

# @Date    : 2020/1/20
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
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        if not head:
            return False

        slow, fast = head, head.next
        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
