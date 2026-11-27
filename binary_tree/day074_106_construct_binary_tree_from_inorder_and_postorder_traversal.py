# 106.从中序与后序遍历序列构造二叉树 / 二叉树 / medium
# 参考解法，待独立补做。

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        positions = {value: i for i, value in enumerate(inorder)}
        stack = [(0, len(inorder) - 1, None, None)]
        post_index = len(postorder) - 1
        root = None

        while stack:
            start, end, parent, side = stack.pop()
            value = postorder[post_index]
            post_index -= 1
            node = TreeNode(value)

            if parent is None:
                root = node
            else:
                setattr(parent, side, node)

            split = positions[value]
            # 后序逆读是根、右、左，右子树最后入栈，先处理。
            if start < split:
                stack.append((start, split - 1, node, "left"))
            if split < end:
                stack.append((split + 1, end, node, "right"))

        return root
