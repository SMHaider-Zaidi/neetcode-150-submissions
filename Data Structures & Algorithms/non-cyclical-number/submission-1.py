class Solution:
    def isHappy(self, n: int) -> bool:

        # Optimal Solution

        seen = set()
        while n != 1:
            n = self.squaresSum(n)
            if n in seen:
                return False
            seen.add(n)
        return True
        
    def squaresSum(self, num):
        curSum = 0

        while num > 0:
            digit = num % 10
            digit = digit * digit
            curSum += digit
            num = num // 10
        return curSum

    # Time: O(logn), Space: O(logn)
    

        


        
        

