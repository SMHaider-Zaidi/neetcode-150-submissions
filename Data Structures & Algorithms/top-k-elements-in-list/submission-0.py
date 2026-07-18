class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Brute Force
        freq_lst = [[] for i in range(len(nums)+1)]

        for num in set(nums): # set() used to not to add duplicates in the list 
            freq = nums.count(num)
            freq_lst[freq].append(num)

        res = []
        for j in range(len(freq_lst)-1, 0, -1):
            for h in freq_lst[j]:
                res.append(h)
                if len(res) == k:
                    return res

        # Time: O(n²), Space: O(n)

 #### Both the solutions uses """BUCKET SORT"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        # Optimized Solution

        # -- We can use hashmap to count frequencies instead of .count()
        #    to optimize time to O(n) from O(n²) --

        freq = [[] for _ in range(len(nums) + 1)]
        
        # Hashmap to count freq in O(n)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 

        for val, frq in count.items():
            freq[frq].append(val)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        


