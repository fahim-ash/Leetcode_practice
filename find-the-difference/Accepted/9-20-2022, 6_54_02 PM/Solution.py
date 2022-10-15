// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        obj={}
       
        for i in s+t:
            if i not in obj:
                obj[i]=1
            else:
                obj[i]+=1
                
            
            
        print(obj)     
        for i in obj:
            if obj[i]%2!=0:
                return i