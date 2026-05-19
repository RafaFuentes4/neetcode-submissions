import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Example: 

        times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
        n = 4
        k = 1

        Output: 3
        """

        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)] #w, n
        visited = set()

        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap) # w1 = 0, n1 = 1

            if n1 in visited:
                continue
            
            visited.add(n1)
            t = max(t, w1)
            
            for n2, w2 in edges[n1]: #w2 = 1, n2 = 2
                heapq.heappush(min_heap, (w1 + w2, n2))
        
        return t if len(visited) == n else -1

        