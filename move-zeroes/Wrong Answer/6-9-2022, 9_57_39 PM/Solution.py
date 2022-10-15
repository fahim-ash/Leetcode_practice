// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zerolist=[]

        for i in nums:
            if i==0:
                nums.remove(i)
                zerolist.append(0)
        z=sorted(nums)
        for j in zerolist:
            nums.append(j)
        nums=z

        
        
        