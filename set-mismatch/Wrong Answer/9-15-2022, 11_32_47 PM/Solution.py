// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            print(nums[i],i+1)
            if nums[i]!=i+1:
                return [i,i+1]
            
            
        