class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Brute Force

        res = []
        for i in range(len(nums)):
            res.append(nums[i]**2)
        res.sort()
        return res

        # Time: O(nlogn), Space: O(1)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Optimal Solution

        res = []
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l]*nums[l] > nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l += 1
            elif nums[r]*nums[r] > nums[l]*nums[l]:
                res.append(nums[r]*nums[r])
                r -= 1
            else:
                res.append(nums[l]*nums[l])
                l += 1
        return res[::-1]

        # Time: O(n), Space: O(n)
