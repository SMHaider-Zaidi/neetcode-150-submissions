class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Brute Force
        zeros = []
        non_zeros = []
        for i in nums:
            if nums[i] == 0:
                zeros.append(i)
            else:
                non_zeros.append(i)
        nums [:] = non_zeros + zeros
        
        return nums

        # Time : O(n), Space: O(n)

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Optimal Solution

        insert = 0
        if nums[0] != 0:
            insert = 1
        for i in range(1, len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1
        return nums
    
        # Time: O(n), Space: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Optimal Solution with lesser operations

        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1
        return nums

        ''' Start from index 0 so every element is processed uniformly.
            If the first element is non-zero, it swaps with itself and insert 
            moves to the next position. '''

        

            