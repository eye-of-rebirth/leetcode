"""
199. 二叉树的右视图 / 二叉树 / middle
思路:层序遍历,只读取每层循环的最右边的数字
卡点:把读取数字的工作放在了while循环里面,而不是for循环里面,在里面限制if多此一举
"""


from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        p = deque([root])
        while p:
            righttokn = p[-1].val
            for i in range(len(p)):
                tokn = p.popleft()
                if tokn.left:
                    p.append(tokn.left)
                if tokn.right:
                    p.append(tokn.right)
            res.append(righttokn)
        return res


