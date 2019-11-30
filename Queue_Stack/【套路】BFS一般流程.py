# -*- coding: UTF-8 -*-

# @Date    : 2019/11/30
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def BFS(self):
        """
        BFS 实现伪代码，需要抓住 3 个关键点：根节点是什么？根节点的一阶邻域节点是哪些？什么时候停止搜索？
        :return:
        """
        # 1. 使用 collections.deque 初始化队列
        # 2. 选择合适的根节点压入队列

        # 3. 使用 while 进入队列循环，直到搜索完毕
        # {
        #   4. 弹出一个节点
        #   5. 放入这个节点周围的节点
        # }
