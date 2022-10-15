// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        z=[]
        for i in nums:
            z.append(i**2)
            
        z.sort()
        return z