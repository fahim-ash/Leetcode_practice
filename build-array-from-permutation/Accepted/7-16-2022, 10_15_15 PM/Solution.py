// https://leetcode.com/problems/build-array-from-permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        list=[]
        for i in nums:
            list.append(nums[i])
            
        return list