# 404.左叶子之和 / 二叉树 / easy

class Solution:
    def sumOfLeftLeaves(self, root):
        stack = [root] if root is not None else []
        total = 0

        while stack:
            node = stack.pop()
            left = node.left

            if left is not None:
                if left.left is None and left.right is None:
                    total += left.val
                else:
                    stack.append(left)

            if node.right is not None:
                stack.append(node.right)

        return total