class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        def feasible(k):
            count = 0

            for n in piles:
                count += math.ceil(n / k)

            return count <= h


        while lo < hi:
            mid = (lo + hi) // 2

            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        