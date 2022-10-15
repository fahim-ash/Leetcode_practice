// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        z={}
        for i in s:
            z[i]=0
            
        for i in z:
            for j in s:
                if i==j:
                    z[i]+=1
        
        l=0
        print(z)
        for i in z:
            if z[i]==1:
                l=i
                return  s.index(l)
          
                        
        return -1