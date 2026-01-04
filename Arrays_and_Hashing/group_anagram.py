# Problem Link: https://neetcode.io/problems/anagram-groups/question?list=neetcode150
# Day 4: Arrays and Hashing
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))  # Sort the string to create a key
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)

        return list(anagrams.values())