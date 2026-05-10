# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, current_val):
            nonlocal result

            if not node:
                return
            
            if node.val >= current_val:
                result += 1
            
            current_val = max(current_val, node.val)


            dfs(node.left, current_val)
            dfs(node.right, current_val)

        dfs(root, float("-inf"))
        return result