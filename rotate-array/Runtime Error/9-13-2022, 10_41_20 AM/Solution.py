// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        list=[]
        for i in range(-k,0):
            list.append(nums[i])
            nums.remove(nums[i])
        for i in range(len(list)):
            nums.insert(i,list[i])
        print(nums,list)
        
        
        
        