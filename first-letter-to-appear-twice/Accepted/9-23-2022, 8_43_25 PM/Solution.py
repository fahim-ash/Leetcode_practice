// https://leetcode.com/problems/first-letter-to-appear-twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        z={}
        for i in s:
            if i in z:
                return i
            z[i]=1
        
        