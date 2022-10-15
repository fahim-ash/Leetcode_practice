// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)+1):
           
            if nums[i-1]!=i:
                return [i-1,i]
            
            
        