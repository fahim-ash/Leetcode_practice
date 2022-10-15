// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[]
        for i in s:
            s1.append(i)
        t1=[]
        for i in t:
            t1.append(i)
        
        s1.sort()
        t1.sort()
        for i in range(len(s1)):
            if s1[i]!=t1[i]:
                return False
        return True
            
        