# -*- coding: UTF-8 -*-

# @Date    : 2020/1/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


# stack迭代，套用模板
class Solution1:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        stack = []
        cur = root
        flag = False

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if flag:
                    return cur
                if cur == p:
                    flag = True
                cur = cur.right
                """
                此处错误的写法：由于误认为stack的上一层
                就会是接下来pop的，但由于stack还可能会继续
                增加元素，所以下一个pop不一定是当前元素的上一层
                cur = stack.pop()
                if cur == p:
                    if stack:
                        return stack.pop()
                    else:
                        flag = True
                if flag:
                    return cur
                """

        return None


# divide & conquer, 结合BST的特点: p的下一个在左边还是右边，不然就正好当前点
class Solution2:

    def inorderSuccessor(self, root, p):
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        else:
            return root
