class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Optimal Solution

        if len(t) > len(s) or t == '': return '' 

        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        start, end = -1, -1
        resLen = float('infinity')
        window = {}
        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    start = l
                    end = r

                window[s[l]] -= 1 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return s[start:end+1] if resLen != float('infinity') else ""
            
        # Time: O(n + m), Space: O(k); 
                                #k = total number of unique characters in s & t




        
        