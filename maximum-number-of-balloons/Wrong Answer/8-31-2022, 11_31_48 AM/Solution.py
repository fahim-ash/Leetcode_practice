// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=0
        b=0
        a=0
        l=0
        o=0
        n=0
        
        
        z="balon"
        list=[]
        for i in z:
            for j in range (len(text)):
                if text[j]==i:
                    list.append(text[j])
                    if text[j]=="b":
                        b+=1
                    if text[j]=="a":
                        a+=1
                    if text[j]=="l":
                        l+=1
                    if text[j]=="o":
                        o+=1
                    if text[j]=="n":
                        n+=1
            
        print(b,a,l,o,n)
        if b==a==n:
            return b
        elif l!=o:
            return 0
        else:
            return 0