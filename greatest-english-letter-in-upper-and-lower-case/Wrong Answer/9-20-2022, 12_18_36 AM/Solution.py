// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case

class Solution:
    def greatestLetter(self, s: str) -> str:
        a=[]
        
        for i in s:
            if i.isupper()==True:
                if i.lower() in s:
                    return i
                
        return ""     
        
        
        