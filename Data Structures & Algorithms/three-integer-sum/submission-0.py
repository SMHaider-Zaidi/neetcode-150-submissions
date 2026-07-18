class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Brute Force

        output = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res = sorted([nums[i], nums[j], nums[k]])
                        if res not in output:
                            output.append(res)
        return output

        # Time: O(n^3), Space: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 

        # Optimal Solution
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            # Two pointers for next two values
            l, r = i + 1, len(nums) - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum < 0:
                    l+=1
                elif curSum > 0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

    # Time: O(n^2), Space: O(1)
        

        
        











