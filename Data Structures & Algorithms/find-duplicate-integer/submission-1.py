class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            count = sum(1 for n in nums if n <= mid)

            if count > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo
        