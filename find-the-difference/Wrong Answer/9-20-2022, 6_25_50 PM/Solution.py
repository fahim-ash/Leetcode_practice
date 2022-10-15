// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        obj={}
       
        for i in s+t:
            count=1
            
            if i in obj:
                count+=1
            obj[i]=count
                
        for i in obj:
            if obj[i]==1:
                return i