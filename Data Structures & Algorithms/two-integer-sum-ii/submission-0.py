class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Brute Force
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return[i+1, j+1]
        
        # Time: O(n^2), Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Optmial Solution
        l, r = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum < target:
                l+=1
            elif curSum > target:
                r-=1
            else:
                return [l+1, r+1]
        
        # Time: O(n), Space: O(1)
             
