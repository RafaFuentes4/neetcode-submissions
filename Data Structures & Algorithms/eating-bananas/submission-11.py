import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right


        def can_eat(k):
            speed = 0

            for bananas in piles:
                speed += math.ceil(bananas / k)
            
            return speed <= h


        while left <= right:
            k = (left + right) // 2

            if can_eat(k):
                right = k - 1
                min_speed = k
            else:
                left = k + 1
        return min_speed
