// https://leetcode.com/problems/largest-3-same-digit-number-in-string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                return num[i:i+3]
        return ""