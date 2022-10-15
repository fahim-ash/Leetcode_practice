// https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        z=['a','e','i','o','u','A','E','I','O','U']
        
        countx=0
        county=0
        for i in range(0,len(s)//2):
            if (s[i]) in z:
                countx+=1
            if (s[len(s)-1-i]) in z:
                county+=1
            
        return countx==county
            
            
            
        
        
          
        