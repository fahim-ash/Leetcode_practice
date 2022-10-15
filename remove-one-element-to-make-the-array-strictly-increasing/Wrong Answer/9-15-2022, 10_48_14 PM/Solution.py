// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        curr=nums[0]
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and len(nums)>2:
                return False
            
            
            if nums[i]<curr:
                print(nums[i])
                
                
                nums.remove(nums[i-1])
                break
                
            else:
                curr=nums[i]
        
        

        z=sorted(nums)        
                
        return z==nums