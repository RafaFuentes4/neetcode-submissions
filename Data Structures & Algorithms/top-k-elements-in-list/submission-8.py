import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        for n in nums:
            count_map[n] += 1
        
        heap = []

        for num in count_map:
            heapq.heappush(heap, (count_map[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]




