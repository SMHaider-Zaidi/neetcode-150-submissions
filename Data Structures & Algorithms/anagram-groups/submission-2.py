# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force

        # hasmap = {}
        # for ch in strs:
        #     sorted_word = "".join(sorted(ch))
        #     if sorted_word in hashmap:
        #         hashmap[sorted_word].append(ch)
        #     else:
        #         hashmap[sorted_word] = [ch]

        # Time: O(m * nlogn) because we sort each of "m" strings and sorting every string of length "n" takes "nlogn"
        # Space: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimized Solution

        hashmap = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count [ord(ch) - ord('a')] += 1

            key = tuple(count)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]

        return list(hashmap.values())

            

