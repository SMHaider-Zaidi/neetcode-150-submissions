class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Brute Force
        sorted_arr = sorted(set(nums))
        max_length  = 0
        for i in sorted_arr: # O(n)
            length =1
            current =i
            while current +1 in sorted_arr: # O(n)   
                length+=1
                current+=1
            if length>max_length:
                max_length = length
        return max_length

        # Time: O(n^2), Space: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Optimized Solution
        sorted_arr = list(set(nums))
        hashmap = {}
        for j in range(len(sorted_arr)):
            hashmap[sorted_arr[j]] = j
        
        max_len = 0
        for i in sorted_arr:
            if i-1 not in hashmap:
                current = i
                length =1
                while current+1 in hashmap:
                    length +=1
                    current+=1
                if length>max_len:
                    max_len = length
        return max_len

        # Time: O(n), Space: O(n)

