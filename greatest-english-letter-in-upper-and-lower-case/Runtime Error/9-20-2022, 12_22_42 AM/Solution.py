// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case

class Solution:
    def greatestLetter(self, s: str) -> str:
       
        
        for i in s:
            if i.isupper()==True:
                if i.lower() in s:
                    a.append(i)

        if len(a)==0:
            return ""
        if a!=None:
            a.sort()
            return a[-1]
        
        
            
        
        
        