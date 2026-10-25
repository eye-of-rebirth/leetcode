"""
145. 二叉树的后序遍历 / 二叉树 / easy
思路:先遍历左子树，再遍历右子树，最后访问根节点。递归实现。

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = []
        postorder(root)
        return res
