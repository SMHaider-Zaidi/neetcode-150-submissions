class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Brute Force

        new = []
        for i in nums:
            if i != val:
                new.append(i)
            
        nums[:] = new
        return len(new)

        # Time: O(n), Space: O(n)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Optimal Solution

        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
        return l

        # Time: O(n), Space: O(1)
