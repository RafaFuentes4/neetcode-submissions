# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, max_val):
            nonlocal result

            if not node:
                return 0

            if node.val >= max_val:
                result += 1
            
            max_val = max(node.val, max_val)

            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, root.val)
        return result