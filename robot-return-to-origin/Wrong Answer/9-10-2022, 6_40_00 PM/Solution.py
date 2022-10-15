// https://leetcode.com/problems/robot-return-to-origin

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count=0
        obj={"U": 2,"D": -2,"L" :1,"R":1}
        for i in moves:
            if i in obj:
                count+=obj[i]
            
        return count==0
            