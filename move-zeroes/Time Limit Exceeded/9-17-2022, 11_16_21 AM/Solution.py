// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]==0:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        """
        Do not return anything, modify nums in-place instead.
        """
        