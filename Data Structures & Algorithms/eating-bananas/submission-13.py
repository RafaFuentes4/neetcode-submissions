import math

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        def feasible(k: int) -> bool:
            current_hours = 0

            for bananas in piles:
                current_hours += math.ceil(bananas / k)
            
            return current_hours <= h


        while lo < hi:
            k = (lo + hi) // 2

            if feasible(k):
                hi = k
            else:
                lo = k + 1
        return lo
        