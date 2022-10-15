// https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        k=[]
        for i in s:
            k.append(i)
        for i in range(len(k)):
            for j in range(i+1,len(k)):
                if k[i]!=k[j]:
                    tmp=k[i]
                    k[i]=k[j]
                    k[j]=tmp
        
        print(k)
        
        return ''.join(k)==goal