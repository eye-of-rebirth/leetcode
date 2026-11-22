# 257.二叉树的所有路径 / 二叉树 / easy

class Solution:
    def binaryTreePaths(self, root):
        result = []
        path = []

        def dfs(node):
            if node is None:
                return

            path.append(str(node.val))

            if node.left is None and node.right is None:
                result.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return result