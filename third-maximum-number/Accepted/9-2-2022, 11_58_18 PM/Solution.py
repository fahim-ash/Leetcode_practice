// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numset = set(nums)
        
        if len(numset) <= 2:
            return max(nums)
        
        else:
            for i in range(2):
                numset = numset - {max(numset)}
                
            return max(numset)
        