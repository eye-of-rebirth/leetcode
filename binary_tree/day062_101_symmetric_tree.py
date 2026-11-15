"""
101.对称二叉树 / 二叉树 / easy
思路：递归比较一对镜像节点，当前值相同且内外两组都对称才成立。
卡点：递归接收两个当前节点，并把两次比较的结果返回。
"""

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def duichen(a, b):
            if a == None and b == None:
                return True
            elif a == None or b == None:
                return False
            if a.val != b.val:
                return False
            return duichen(a.left, b.right) and duichen(a.right, b.left)

        return duichen(root.left, root.right)