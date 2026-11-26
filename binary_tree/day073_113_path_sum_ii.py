# 113.路径总和 II / 二叉树 / medium
# 参考解法，待独立补做。

class Solution:
    def pathSum(self, root, targetSum):
        if root is None:
            return []

        result = []
        path = []
        stack = [(root, targetSum)]

        while stack:
            node, remaining = stack.pop()
            if node is None:
                path.pop()
                continue

            path.append(node.val)
            remaining -= node.val

            if node.left is None and node.right is None and remaining == 0:
                result.append(path.copy())

            stack.append((None, 0))  # 退出当前节点时撤销路径。
            if node.right is not None:
                stack.append((node.right, remaining))
            if node.left is not None:
                stack.append((node.left, remaining))

        return result
