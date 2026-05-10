# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, current_depth):
            if not node:
                return

            if current_depth == len(result):
                result.append(node.val)

            dfs(node.right, current_depth + 1)
            dfs(node.left, current_depth + 1)

            
        dfs(root, 0)
        return result
        