// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==0:
                nums.pop(nums[i])
                nums.append(0)
        
        