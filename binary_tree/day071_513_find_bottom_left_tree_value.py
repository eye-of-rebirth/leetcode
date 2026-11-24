# 513.找树左下角的值 / 二叉树 / medium

from collections import deque


class Solution:
    def findBottomLeftValue(self, root):
        queue = deque([root])

        while queue:
            leftmost = queue[0].val
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return leftmost