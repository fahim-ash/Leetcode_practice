// https://leetcode.com/problems/keep-multiplying-found-values-by-two

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        
        for i in nums:
           
            
            
            if i%original==0 and i*2 not in nums:
                return i*2
                
       