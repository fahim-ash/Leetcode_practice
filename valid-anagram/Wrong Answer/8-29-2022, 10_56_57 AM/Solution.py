// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        t1={}
        for i in s:
            s1[i]=i
        for i in t:
            t1[i]=i
            
            
        for i in s1:
            if i not in t1:
                return False
        for i1 in t1:
            if i1 not in s1:
                return False
        
        
        if len(s1)!=len(t1):
            return False
        return True
        