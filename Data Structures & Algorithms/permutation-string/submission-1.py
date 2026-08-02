class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Optimal Solution
        '''Fixed-size sliding window + frequency map. '''

        if len(s1) > len(s2):
            return False

        countS1 = {}
        countS2 = {}

        # Frequency of s1
        for ch in s1:
            countS1[ch] = countS1.get(ch, 0) + 1

        l = 0
        for r in range(len(s2)):
            countS2[s2[r]] = countS2.get(s2[r], 0) + 1

            if (r - l + 1) == len(s1):
                if countS1 == countS2:
                    return True
            
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l += 1

        return False
        
        # Time: O(26 * n) = O(n)
        # Space: O(26) = O(1)

