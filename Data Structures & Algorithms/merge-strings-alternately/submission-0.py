class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Optimal Solution

        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
        # Time: O(n), Space: O(n)

        ''' Use a list because appending is O(1) amortized.
        Strings are immutable, so repeated concatenation creates new strings (O(n)).

        
        Join once at the end instead of creating new strings repeatedly.'''

        