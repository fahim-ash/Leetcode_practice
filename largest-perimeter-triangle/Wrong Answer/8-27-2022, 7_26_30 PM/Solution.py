// https://leetcode.com/problems/largest-perimeter-triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        z=sorted(nums)
        count=0
        if (z[-3]+z[-2])<z[-1]:
            pass
            
        else:
            count+=z[-1]+z[-2]+z[-3]
            
        return count
            
        