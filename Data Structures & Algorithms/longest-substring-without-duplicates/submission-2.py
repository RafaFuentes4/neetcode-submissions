class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            Input: s = "zxyzxyz"
            Output: 3
        """

        char_set = set()
        l = 0
        
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring


        