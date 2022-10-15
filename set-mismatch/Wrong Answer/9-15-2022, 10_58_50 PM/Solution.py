// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
                return ([nums[i+1],nums[i]+1])
            
        