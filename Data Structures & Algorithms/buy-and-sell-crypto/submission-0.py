class Solution1:
    def maxProfit(self, prices: List[int]) -> int:

        # Brute Force

        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[l]
                max_profit = max(max_profit, profit)
        return max_profit

        # Time: O(n^2), Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Optimal Solution

        max_profit = 0
        l, r = 0, 1

        while l < r and r < len(prices):

            if prices[l] < prices[r]:   

                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1

            else:
                l = r
                r += 1                
        return max_profit

        # Time: O(n), Space: O(1)
        