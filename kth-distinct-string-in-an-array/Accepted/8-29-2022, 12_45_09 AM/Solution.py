// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        count=0
        for u,v in d.items():
            if v==1:
                count+=1
            if count==k:
                return u
                
        return ""
        
        
       