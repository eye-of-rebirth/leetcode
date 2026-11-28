# 105.从前序与中序遍历序列构造二叉树 / 二叉树 / medium
# 参考解法，待独立补做。

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        positions = {value: index for index, value in enumerate(inorder)}
        root = TreeNode(preorder[0])
        stack = [(root, 0, len(inorder) - 1, 0)]

        while stack:
            node, start, end, pre_start = stack.pop()
            split = positions[node.val]
            left_size = split - start

            if split < end:
                right_start = pre_start + 1 + left_size
                node.right = TreeNode(preorder[right_start])
                stack.append((node.right, split + 1, end, right_start))
            if start < split:
                left_start = pre_start + 1
                node.left = TreeNode(preorder[left_start])
                stack.append((node.left, start, split - 1, left_start))

        return root
