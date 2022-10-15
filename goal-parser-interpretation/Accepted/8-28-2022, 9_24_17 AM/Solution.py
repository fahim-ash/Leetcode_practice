// https://leetcode.com/problems/goal-parser-interpretation

class Solution:
    def interpret(self, command: str) -> str:
        word="" 
        l=[]
        for i in command:
            l.append(i)
        
        for j in range(1,len(command)):
            if l[j-1]=="(" and l[j]==")":
                word+="o"
            
            else :
                if l[j-1]!="(" and l[j-1]!=")":
                    word+=l[j-1]
                    
        if command[-1]=="G":
                    word+="G"
            
        return word