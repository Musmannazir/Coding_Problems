# Problem link: https://neetcode.io/problems/is-anagram/question?list=neetcode150
# Day 2: Arrays and Hashing
class Solution: 
      def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for e in s:
            count_s[e] = count_s.get(e,0)+1
        for d in t:
            count_t[d] = count_t.get(d,0)+1

        return count_s == count_t 
