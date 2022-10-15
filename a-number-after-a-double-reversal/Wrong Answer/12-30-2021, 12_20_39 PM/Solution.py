// https://leetcode.com/problems/a-number-after-a-double-reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return "true"
        elif num%10==0:
            return "false"
        elif num%10!=0:
            return "true"
        else:
            return "false"
        