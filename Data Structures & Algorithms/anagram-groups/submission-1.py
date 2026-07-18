class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force

        hashmap = {} # sorted_word : [list of anagrams]
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(i)
            else:
                hashmap[sorted_word] = [i]
        return list(hashmap.values())

        # Time: O(m * nlogn) because we sort each of "m" strings and sorting every string of length "n" takes "nlogn"
        # Space: O(n)
# class Solution1:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Optimized Solution