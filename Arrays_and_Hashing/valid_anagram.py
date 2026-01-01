# Problem link: https://neetcode.io/problems/is-anagram/question?list=neetcode150
# Day 2: Arrays and Hashing
class Solution: 
      def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = count_s.get(c,0)+1
        for d in t:
            count_t[d] = count_t.get(d,0)+1

        return count_s == count_t 
