class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Brute Force
        op = []
        res = 1
        for i in range(len(nums)): #O(n)
            j = len(nums)-1
            while j>=0: # O(n) => runs for every value of "i"
                if i!=j:
                    res *= nums[j]
                j-=1
            op.append(res)
            res = 1
        return op

        # Time: O(n^2), Space: O(n)

        # One more Brute Force
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ans[i] *= nums[j]

        return ans
        '''
        # Time: O(n^2), Space: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Optimized Solution
        # prefix = [1]*len(nums)
        # suffix = [1]*len(nums)
        # ans = [1]*len(nums)
        # for i in range(1, len(nums)):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        # for j in range(len(nums)-2, 0, -1):
        #     suffix[j] = suffix[j+1] * nums[j+1]
        # for k in range(len(nums)):
        #     ans[i] = prefix[k] * suffix[j]
        # return ans

        ''' 
        This solution is optimized Time: O(n) and Space: O(n)
        BUT we also have to optimize it for O(1) Space Complexity.

        Therefore, we won't make two extra lists => Prefix and Sufix
        1. First we will store prefix in output list
        2. Then by iterating the nums array backwards we will calculate the
            sufffix and store it in output list by multiplying 
            the prefix already stored there.

        Time: O(n)
        Space: O(1) (excluding the output array)
        '''
        ans = [1] * len(nums) # output list

        for i in range(1, len(nums)):
            # Calculate prefix and store it in ans
            ans[i] = ans[i-1] * nums[i-1]
            
        suffix = 1
        for j in range(len(nums)-2, -1, -1):
            suffix *= nums[j+1]
            ans[j] *= suffix
        return ans


        #Time: O(n)
        #Space: O(1) (excluding the output array) 








