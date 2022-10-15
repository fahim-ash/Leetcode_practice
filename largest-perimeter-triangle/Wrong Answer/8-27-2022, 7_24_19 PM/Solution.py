// https://leetcode.com/problems/largest-perimeter-triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        z=sorted(nums)
        if len(z)>3:
            z = list(dict.fromkeys(z))
        count=0
        if (z[1]+z[0])<=z[2]:
            pass
            
        else:
            count+=z[0]+z[1]+z[2]
            
        return count
            
        