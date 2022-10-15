// https://leetcode.com/problems/lemonade-change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count=0
        for i in bills:
            i=int(i)
            count=count+i

        if count%10==5:
            return "true"
        else:
            return "false"
