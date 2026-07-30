class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Optimal Solution

        l = 0
        maxLen = 0
        count = {}

        for r in range(len(s)): # O(n)
            count[s[r]] = count.get(s[r], 0) + 1

            if (r-l+1) - max(count.values()) > k:   # max(count.values())-->O(26)
                count[s[l]] -= 1
                l += 1
            else:
                maxLen = max(maxLen, r-l+1)
        return maxLen

        # Since there are only 26 upper case letters
        # Time: O(26.n), Space: O(26)/O(1)
             