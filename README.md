# LCtrip in :snake:
  Code OJ note in python3 - - We care about coding style here ! 白板编程面试模板代码，保证Coding Style前提下，最短最高效

# 前言
- 题目来源包括： LeetCode、LintCode、Cracking the coding interview、ACM challenge workbook(挑战程序设计竞赛)
- 本项目的target是白板编程时可以清晰简练的手写代码，好的coding style函数名，变量名自解释，而不用大量注释。同时在保证写法最佳情况下，最求代码量最短
- 项目持续更新中，优先使用 python3，如果您有coding style更有利于面试的写法希望分享的话欢迎联系更新~  
- 如果您对当前解析有任何疑问，咱们 issue 见~

# :trophy: 里程碑
- 🧬 版图
	- [🐤 Breadth First Search](#-bfs)
	- [🐑 Binary Tree](#-binary-tree)
	- [🦌 Binary Search](#-binary-search)
	- [🦎 Two Pointer](#-two-pointer)
	- [🐄 Deep First Search](#-dfs)
    - [🦉 Dynamic Programming](#-bfs)

# 题库解析
此专栏保证Coding Style前提下，最短最高效。

### 🐤 Breadth First Search
- Bfs写法简单清晰，以下是使用场景
- 图的遍历 Traversal in Graph
    - 层级遍历 Level Order Traversal
    - 由点及面 Connected Component
    - 拓扑排序 Topological Sorting
- 最短路径 Shortest Path in Simple Graph
    - 仅限简单图求最短路径
    - 即，图中每条边长度都是1，且没有方向
- 能够用 BFS 解决的问题，一定 不要用 DFS 去做！

#### LintCode 618.Search graph nodes
- Bfs 分层和不分层
```python
from collections import deque

class Solution:
    def searchNode(self, graph: List[Node], values: dict, node:'Node', target:int)->'Node':

        q = deque([node])
        seen = set()
        seen.add(node)

        while q:
            head = q.popleft()
            if values[head] == target:
                return head

            for nei in head.neighbors:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)

        return None

# Follow up: 如何找到所有最近的value=target的点: BFS分层
class Solution:
    def searchNode(self, graph: List[Node], values: dict, node:'Node', target:int)->List[Node]:

        q = deque([node])
        seen = set()
        seen.add(node)
        res = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if values[node] == target:
                    res.append(node)
                    for nei in node.neighbors:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
            if res:
                return res

        return None
```

### 🐑 Binary Tree
- 碰到二叉树的问题，就想想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么
- Dfs用递归实现分为 Divide Conquer 和 Traverse, Divide Conquer更为简单直接，90%问题可解决

#### 94.Binary Tree inorder traversal
```python
# Non-recursion
class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)  # add after all left children
                cur = cur.right

        return res
```

#### 145.Binary Tree Postorder traversal
```python
from collections import deque

# Use deque, non-recursion
class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = deque([])

        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                res.appendleft(cur.val)  # reverse process of preorder
                cur = cur.right          # reverse process of preorder
            else:
                node = stack.pop()
                cur = node.left          # reverse process of preorder
        return res
```
### 🦌 Binary Search
- 二分查找是很多其他算法的基础，比如快搜
- 二分法基本功
    - 时间复杂度小练习
    - 递归与非递归的权衡
    - 二分的三大痛点
    - 通用的二分法模板
- 第一境界：二分位置 之 圈圈叉叉 Binary Search on Index - OOXX
    - 找到满足某个条件的第一个位置或者最后一个位置
- 第二境界：二分位置 之 保留一半 Binary Search on Index - Half half
    - 保留有解的一半，或者去掉无解的一半
- 第三境界：二分答案 Binary Search on Result
    - 压根看不出是个二分法！
- 根据要求的时间复杂度倒推求解算法

#### 34. Find First and Last Position of Element in Sorted Array
- Partition的标准实现
```python
# 二次无脑二分模板first and last， Todo：可有更好的coding style
class Solution1:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1, -1]
        if not nums:
            return res
        
        # find first appear
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end
        
        # find last appear
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            res[1] = start
        elif nums[start] == target:
            res[1] = end

        return res

# 更机智的方法，只用一种binery search，用python自带的bisect可
import bisect

class Solution2:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = bisect.bisect_left(nums, target)
        # 因为有序性
        last = bisect.bisect_left(nums, target + 1)

        # the indices will be equal only if the target is not in the list
        if first == last:
            return [-1, -1]

        # last是最后一个目标值的下一个位置
        return [first, last - 1]
```

### 🦎 Two Pointer
- 灵活运用quick sort和quick selection中的partition过程
- 对于求 2 个变量如何组合的问题，可以循环其中一个变量，然后研究另外一个变量如何变化
- 双指针问题也可以考虑hash解，看哪个更符合要求。双指针有同向（一般O(n^2))和异向(一般O(n))。
- Two sum若干变种，要熟练

#### LintCode 31.Partition array
- Partition的标准实现
```python
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 当跳出循环时 left > right， 而此时left其实指在原来right区域的第一个值，所以可以保证left的前的所有元素都是<k
        return left
```

#### 215.Kth largest element in an array
- Quick select的标准实现
```python
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k) # 举个例子就能发现，kth小和kth大互相转换是len(nums)-k

    def quickSelect(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quickSelect(nums, start, right, k)
        if k >= left:
            return self.quickSelect(nums, left, end, k)

        # right < k < left:
        return nums[k]
```

#### LintCode 463.Sort integers
- Quick sort的标准实现
```python
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        if not nums:
            return

        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        # 1. pivot, nums[start], nums[end]
        # get value not index
        pivot = nums[(start + end) // 2]

        # 2. left <= right not <
        while left <= right:  
            while left <= right and nums[left] < pivot: # not <=
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
```

#### 15.3Sum
- K sum问题的标准解法，很好的coding style
```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], result)

    def find_two_sum(self, nums, left, right, target, result):
        value = nums[left] + nums[right]
        while left < right:
            if value == target:
                result.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif value > target:
                right -= 1
            else:
                left += 1
```
