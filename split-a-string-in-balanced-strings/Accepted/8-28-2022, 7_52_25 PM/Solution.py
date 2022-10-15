// https://leetcode.com/problems/split-a-string-in-balanced-strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        secondCount=0
        count=0
        for i in s:
            
            if i=="R":
                count+=1
            if i=="L":
                count-=1
            if count==0:
                secondCount+=1
        
        return secondCount
            
            
        