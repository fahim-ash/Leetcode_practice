// https://leetcode.com/problems/sorting-the-sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        z=list(s.split(" "))
        
        a=[]
        m=1
        for i in range(len(z)):
            for j in range(len(z)):
          
                if int(z[j][-1])==m:
                    
                    a.append(z[j])
                    m=m+1
 
        output=""
    
        
        for i in range(len(a)):
            output=output+(a[i][0:-1])+" "
            
      
            
            
            
    
        return output[0:-1]
            
        
        
            
        
        