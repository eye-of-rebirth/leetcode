"""
94.二叉树的中序遍历 / 二叉树 / easy
思路:中序遍历就是先进行左边的遍历,然后访问根节点,最后进行右边的遍历,根节点就是当前节点
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res
