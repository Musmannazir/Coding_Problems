# problem link: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150
# Day 3: Arrays and Hashing
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
