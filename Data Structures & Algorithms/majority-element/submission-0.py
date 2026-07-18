class Solution1:
    def majorityElement(self, nums: List[int]) -> int:

        # Sub-optimal Solution

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        
        for value, freq in hashmap.items():
            if freq > len(nums) // 2:
                return value

        # Time: O(n), Space: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Optimal Solution for Space Complexity

        res = 0
        count = 0
        for i in nums:
            if count == 0:
                res = i
            count += ( 1 if i == res else -1)

        return res

        # Time: O(n), Space: O(1)









        