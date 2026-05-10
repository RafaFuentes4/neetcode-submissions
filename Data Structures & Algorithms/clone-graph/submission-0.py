"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        node_map = {}
        seen = set()

        def dfs(node):
            node_map[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        node_map[node] = Node(val = node.val)
        seen.add(node)
        dfs(node)

        for old_node in node_map:
            new_node = node_map[old_node]
            for old_nei in old_node.neighbors:
                new_neighbor = node_map[old_nei]
                new_node.neighbors.append(new_neighbor)

        return node_map[node]




        