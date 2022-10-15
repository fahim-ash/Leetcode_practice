// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort()
        for i in nums:
            if i==0:
                nums.pop(i)
                nums.append(0)
        