class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force 
        #=====================================
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # Time: O(n^2), Space: O(1)

        # Optimized Solution
        #=====================================
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i
        # Time: O(n), Space: O(n)





