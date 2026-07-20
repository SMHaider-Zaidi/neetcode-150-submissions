class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Optimal Solution
    
        l, r = 0, 0
        while l < len(s):
            while r < len(t) and t[r] != s[l]:
                r += 1
            if r == len(t):  
                return False
            l += 1
            r += 1
        return True
        
    # Time: O(n  + m), Space: O(1)

