"""
102. 二叉树的层序遍历 / 二叉树 / medium
思路:使用队列进行层序遍历，将每一层的节点值存储在列表中，并将列表添加到结果列表中
时间复杂度：O(n)，其中 n 是二叉树的节点数。每个节点都被访问一次。
空间复杂度：O(n)，其中 n 是二叉树的节点数。队列中最多包含 n 个节点。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# 引用队列

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        q = deque([root])  # 栈,队列,递归函数里面装的是二叉树类型,答案list里面装的是int

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
