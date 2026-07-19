class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Brute Force

        return len(set(nums))

        # Time: O(n), Space: O(n)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Optimized Solution for O(1) Space Complexity

        if not nums: return 0

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l

        # Time: O(n), Space: O(1)

        

