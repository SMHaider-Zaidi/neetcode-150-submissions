class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Brute Force
        #======================================================
        # if len(s) != len(t):
        #     return False
        # for ch in s:
        #     if s.count(ch) != t.count(ch):
        #         return False
        # return True
        # Time: O(n^2) , Space: O(1)

        # Optimized Solutions
        #=======================================================

        #01:
        # return sorted(s) == sorted(t) --> Time:O(nlogn), Space: O(n) bcz sorted() creates a list 

        #02:
        #return Counter(s) == Counter(t)

        #03:
        #-------using hashmap-------

        hmapS, hmapT = {}, {}

        if len(s) != len(t):
            return False
        for ch in s:
            if ch in hmapS:
                hmapS[ch] += 1
            else:
                hmapS[ch] = 1
        for ch in t:
            if ch in hmapT:
                hmapT[ch] += 1
            else:
                hmapT[ch] = 1

        return hmapS == hmapT

        # Time: O(n + m) or O(n)
        # Space: O(1) --> because s and t contains lower case letters only O(26).



