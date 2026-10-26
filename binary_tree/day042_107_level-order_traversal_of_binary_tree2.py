"""
107. 二叉树的层序遍历 II / 二叉树 / middle
思路:本质上就是层序遍历,只是最后把结果reverse一下
卡点:注意if 和elif 的区别
"""



from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        q = deque([root])

        while q:
            level =[]
            for _ in range(len(q)):
                node =q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                #注意如果用的是elif 就是说只有一个是成立的,不适应于这道题
                if node.right:
                    q.append(node.right)
            res.append(level)
        res.reverse()
        return res