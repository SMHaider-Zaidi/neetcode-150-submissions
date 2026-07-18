class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Optimal solution

        n = len(nums)
        hashSet = set(nums)
        res = []
        for i in range(1, len(nums)+1): # O(n)
            if i not in hashSet: # O(1)
                res.append(i)
        return res

        # Time: O(n), Space: O(n)
