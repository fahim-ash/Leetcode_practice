// https://leetcode.com/problems/smallest-index-with-equal-value

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            if(i%10==nums[i]):
                a.append(i)
        if(len(a)>0):
            return a[0]
        else:
            return -1
        