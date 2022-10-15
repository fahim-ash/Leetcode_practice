// https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s={}
        for i in words[0]:
            s[i]=0
        
        for k in words:
            
            for i in k:
                count=0
                
                if i in s:
                    count+=1
                    s[i]+=count


        z=[]
        for i in s:
            if s[i]<3:
                pass
            
            else:
                for j in range(s[i]//3):
                    z.append(i)
                
        return z
                
        
                    
        