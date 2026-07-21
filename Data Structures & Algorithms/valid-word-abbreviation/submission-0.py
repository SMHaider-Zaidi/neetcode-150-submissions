class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # Optimal Solution

        l = 0
        r = 0
        while l < len(word) and r < len(abbr):
            if abbr[r].isalpha():
                if word[l] != abbr[r]:
                    return False
                l += 1
                r += 1
            else:
                if abbr[r] == '0':
                    return False
                skip = ''
                while r < len(abbr) and abbr[r].isdigit():
                    skip += abbr[r]
                    r += 1
                l += int(skip)
        return l == len(word) and r == len(abbr) 

        # Time: O(n + m), Space: O(1)
    
                

        
            

