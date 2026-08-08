class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Brute Force

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False

        # Time: O(n^2), Space: O(1)

class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Optimal Solution
        if k == 0: return False

        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if abs(hashmap[nums[i]] - i) <= k:
                    return True
        return False

        # Time: O(n), Space: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Optimal Solution # 02

        window = set()
        
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False

        # Time: O(n), Space: O(n)


