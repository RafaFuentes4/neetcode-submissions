class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0] * n
        prefix = [0] * n 
        postfix = [0] * n

        prefix[0] = 1
        postfix[n - 1] = 1

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res


        