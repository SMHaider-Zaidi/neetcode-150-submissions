class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Brute Force

        nums1[m:] = nums2
        nums1.sort()

        # Time: O(nlogn), Space: O(n)
    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Optimal Solution

        insert = m + n - 1
        p1 = m-1
        p2 = n-1

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[insert] = nums2[p2]
                p2 -= 1
            else:
                nums1[insert] = nums1[p1]
                p1 -= 1
            insert -= 1

        while p2 >= 0:
            nums1[insert] = nums2[p2]
            insert -= 1
            p2 -= 1


        # Time: O(m+n), Space: O(1)


        
