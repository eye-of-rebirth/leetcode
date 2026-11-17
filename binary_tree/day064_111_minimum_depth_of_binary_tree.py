"""
111.二叉树的最小深度 / 二叉树 / easy
思路:递归求最小深度，单侧为空时沿另一侧，两侧都有时取较小值再加一
卡点：空孩子不代表叶子，不能直接参与取最小值
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def minfind(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if not root.left and root.right:
                r = minfind(root.right)
                return r + 1
            elif not root.right and root.left:
                l = minfind(root.left)
                return l + 1
            else:
                r = minfind(root.right)
                l = minfind(root.left)
                return min(r, l) + 1

        res = minfind(root)
        return res