"""
226.翻转二叉树 / 二叉树 / easy
思路：递归访问每个节点，交换左右孩子，返回原根节点。
卡点：明确递归处理对象，以及遇到 None 时停止。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def reverse(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            reverse(root.left)
            reverse(root.right)

        reverse(root)
        return root