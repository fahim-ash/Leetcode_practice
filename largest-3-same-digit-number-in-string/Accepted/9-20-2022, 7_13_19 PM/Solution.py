// https://leetcode.com/problems/largest-3-same-digit-number-in-string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        list=[]
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                list.append ( num[i:i+3])
        list.sort()
        if len(list)==0:
            return ""
        return list[-1]