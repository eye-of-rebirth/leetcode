"""
104.二叉树的最大深度 / 二叉树 / easy
思路:递归求左右子树深度，取较大值加 1
卡点：区分传入的节点与返回的深度，先拿子树结果再计算。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def zuidasd(root):
            if not root.left:
                l = 0
            else:
                l = zuidasd(root.left)
            if not root.right:
                r = 0
            else:
                r = zuidasd(root.right)
            res = max(l, r) + 1
            return res

        return zuidasd(root)
