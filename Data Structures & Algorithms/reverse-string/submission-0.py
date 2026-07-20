class Solution1:
    def reverseString(self, s: List[str]) -> None:

        # Brute Force
        s[:] = s[::-1]

        # Time: O(n), Space: O(n)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Optimal Solution

        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

        # Time: O(n), Space: O(1)

            
        