import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        for n in nums:
            count_map[n] += 1
        
        heap = []

        for n in count_map:
            heapq.heappush(heap, (count_map[n], n))
            
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result
