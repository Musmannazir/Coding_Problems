# problem link: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
# Day 1: Arrays and Hashing
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
