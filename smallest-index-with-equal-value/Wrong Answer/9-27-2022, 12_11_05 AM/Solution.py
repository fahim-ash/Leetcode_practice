// https://leetcode.com/problems/smallest-index-with-equal-value

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            z=i%10
            if z==nums[i]:
                count=nums[i]
                return count
            
          
        return -1
        