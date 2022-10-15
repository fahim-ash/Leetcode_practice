// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        curr=nums[-1]
        count=0
        for i in range(1,nums[-1]):
            if curr<=0:
                break
            else:
                count+=1
                curr=curr-i
                
        
                
                
        return count    
            
        