// https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        z=[]
        for i in range(0,len(nums)):
                if target==nums[i]:
                        z.append(i)
                        
        return z
        