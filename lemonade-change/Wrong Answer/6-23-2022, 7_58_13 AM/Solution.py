// https://leetcode.com/problems/lemonade-change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills =[5,5,10,10,20]
        count=0
        for i in bills:
            i=int(i)
            count=count+i

        if count%10==0 or count%10!=5:
            return "false"
        else:
            return "true"
