class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute Force
        #===========================
        # seen = []
        # for i in nums:
        #     if i not in seen:
        #         seen.append(i)
        # return len(seen) != len(nums)
        #=============================
        # Time: O(n^2), Space: O(n)

        # Optimized Solution
        return len(set(nums)) != len(nums)
        # Time: O(n), Space: O(n)
                
