// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    print("yes",nums[i])
                    if (i*j)%2==0:
                        count+=1
                        
        return count
                
            
        