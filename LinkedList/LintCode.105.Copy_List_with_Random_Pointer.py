# -*- coding: UTF-8 -*-

# @Date    : 2020/1/12
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


# 使用hashmap
class Solution1:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head

        # mapping the node
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = RandomListNode(cur.label)
            cur = cur.next

        # copy the next and random pointer
        for node in mapping:
            newNode = mapping[node]
            if node.next:
                newNode.next = mapping[node.next]
            if node.random:
                newNode.random = mapping[node.random]

        return mapping[head]


# 不使用额外空间
class Solution2:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        cur = head
        while cur:
            copy = RandomListNode(cur.label)
            tmp = cur.next
            cur.next = copy
            copy.next = tmp
            cur = tmp

        cur = head
        newhead = cur.next
        while cur:
            copy = cur.next
            tmp = copy.next
            if tmp:
                copy.next = tmp.next
            if cur.random:
                copy.random = cur.random.next
            cur = tmp

        return newhead
