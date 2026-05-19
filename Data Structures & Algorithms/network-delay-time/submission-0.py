import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #me dan times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]

        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        """
        edges = {
            1: [(2, 1), (4, 4)],
            2: [(3, 1)],
            3: [(4, 1)],
        }
        """

        min_heap = [(0, k)] #(dist, node) <- root
        visited = set()

        t = 0
        
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1+w2, n2))
                
        return t if len(visited) == n else -1

