// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        z={}
        for i in nums:
            z[i]=0
            
        for i in z:
            for j in nums:
                if i==j:
                    z[i]+=1
                    
        for i in z:
            if z[i]==1:
                return True
        return False
        