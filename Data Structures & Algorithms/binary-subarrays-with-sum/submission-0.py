class Solution1:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # Brute Force

        count = 0 
        for i in range(len(nums)):
            cur_sum = 0 
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum == goal:
                    count += 1
        return count

        # Time: O(n^2), Space: O(1)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # Optimized Solution
        '''Prefix Sum + hashmap'''

        res = 0
        prefixSum = { 0 : 1 }
        cur_sum = 0
        for n in nums:
            cur_sum += n
            diff = cur_sum - goal

            res += prefixSum.get(diff, 0)
            prefixSum[cur_sum] = 1 + prefixSum.get(cur_sum, 0)
        return res

        # Time: O(n), Space: O(n)

