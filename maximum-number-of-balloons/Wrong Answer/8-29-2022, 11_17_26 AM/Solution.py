// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=0
        z="balon"
        list=[]
        for i in z:
            for j in text:
                if i==j:
                    list.append(j)
                    count+=1
       
        if count<7:
            return 0
        else:
            return count//7
            
        