# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result = 0

        def dfs(node, current_max):
            nonlocal result

            if not node:
                return

            if node.val >= current_max:
                result += 1
                current_max = node.val

            dfs(node.left, current_max)
            dfs(node.right, current_max)

        dfs(root, float("-inf"))
        return result

        