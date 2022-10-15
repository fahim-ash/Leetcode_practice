// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1={}
        s2={}
        for i in ransomNote:
            if i not in s1:
                s1[i]=1
            else:
                s1[i]+=1
                
        for i in magazine:
            if i  not in s2:
                s2[i]=1
            else:
                s2[i]+=1   
        
   
        for i in s1:
            
            
            if i not in s2 or s2[i]<s1[i]:
                return False
            
        return True
            
            
        
            
            
        