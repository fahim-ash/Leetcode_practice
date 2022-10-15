// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s=="":
            return t
        
        for i in t:
            if i not in s:
                return i
        
        return t[-1]
    
       
        