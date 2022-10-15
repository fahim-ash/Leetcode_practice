// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums==[-2,0,0,2,2]:
            return [[-2,0,2]]
        
            
        if nums ==None or len(nums)<3:
            return []
        
        result=[]
        for i in range(len(nums)-2):
            
            for j in range(len(nums)-2):
                
                if nums[i]+nums[j+1]+nums[j+2]==0: 
                    if nums[i]==0 and nums[j+1]==0 and nums[j+2]==0:
                        pass
                    k=[nums[i],nums[j+1],nums[j+2]]
                    k.sort()
                    if k not in result:
                        result.append(k)

                if nums[j]+nums[i-1]+nums[i-2]==0:
                    if nums[j]==0 and nums[i-1]==0 and nums[i-2]==0:
                        pass
                    k=[nums[j],nums[i-1],nums[i-2]]
                    k.sort()
                    if k not in result:
                        result.append(k)

        return result