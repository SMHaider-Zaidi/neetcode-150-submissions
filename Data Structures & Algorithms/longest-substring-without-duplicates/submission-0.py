class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Brute Force

        count = 0
        max_count = 0
        seen = set()

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    count+=1
                    max_count = max(max_count, count)
        return max_count

        # Time: O(n^2), Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Optimal Solution
        ''' Sliding Window ''' 

        res = 0
        charSet = set()

        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

        # Time: O(n), Space: O(1)





        