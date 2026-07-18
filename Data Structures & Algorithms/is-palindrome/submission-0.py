class Solution1:
    def isPalindrome(self, s: str) -> bool:
        
        # Brute Force

        filtered = ''
        for i in s:
            if i.isalnum():
                filtered += i.lower()
        return filtered == filtered[::-1]

        # Time: O(n), Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Optimized Solution
        l, r = 0, len(s) -1
        while l < r:
            while l<r and not self.isAlnum(s[l]):
                l += 1
            while r>l and not self.isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        
    def isAlnum(self, ch):
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))
