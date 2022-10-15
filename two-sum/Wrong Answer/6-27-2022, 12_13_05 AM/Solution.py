// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=0
        new=[]
        for i in range(len(nums)-1):
            if nums[i]<target and sum<target:
                sum=sum+nums[i]
                new.append(i)
                
        return new
        