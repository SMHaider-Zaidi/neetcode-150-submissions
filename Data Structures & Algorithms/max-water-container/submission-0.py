class Solution1:
    def maxArea(self, heights: List[int]) -> int:

        # Brute Force

        max_area = 0 
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                w = j-i
                h = min(heights[i], heights[j])
                area = (w*h)
                max_area = max(max_area, area)
        return max_area

        # Time: O(n^2), Space: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Optimal Solution

        max_area = 0

        l, r = 0, len(heights)-1
        while l < r:
            area = (r-l) * (min(heights[l], heights[r]))
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                r-=1        # Move any one pointer
        return max_area

        # Time: O(n), Space: O(1)
        
