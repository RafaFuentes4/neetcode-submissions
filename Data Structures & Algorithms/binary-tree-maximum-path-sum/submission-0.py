# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node): #devuelve el path_sum (izquierda + derecha )
            nonlocal max_path

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_max = max(0, left)
            right_max = max(0, right)

            max_path = max(max_path, left_max + right_max + node.val)

            return node.val + max(left_max, right_max)
            
        dfs(root)
        return max_path