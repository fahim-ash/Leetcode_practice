// https://leetcode.com/problems/divide-array-into-equal-pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        same=[]
        for i in range(len(nums)):
                       
            for j in range(i+1,len(nums)):
                       if nums[i]==nums[j]:
                        same.append(nums[i])
   
                      
        for i in nums:
            if i not in same:
                return False
            return True
            
        