class Solution:
    def trap(self, height: List[int]) -> int:

        # Brute Force

        water = 0

        for i in range(len(height)):
            leftMax = max(height[:i+1])
            rightMax = max(height[i:])

            water += min(leftMax, rightMax) - height[i]

        return water

        # Time: O(n²), Space: O(n) -> cause of slicing

''' 
>>> For every index, find the tallest bar on its left and right using max().
>>> Water stored = min(leftMax, rightMax) - current height. 
'''




