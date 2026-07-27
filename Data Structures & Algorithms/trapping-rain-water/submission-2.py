class Solution1:
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

class Solution:
    def trap(self, height: List[int]) -> int:

        # Optimal Solution

        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        water_trapped = 0

        while l < r:
            if leftMax < rightMax:
                water_trapped += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                water_trapped += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])
        return water_trapped

        # Time: O(n), Space: O(1) 
        




