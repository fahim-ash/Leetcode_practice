// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        obj={}
        for i in nums:
            obj[i]=1
        list=[]
        for i in obj:
            list.append(i)
        if len(list)==2:
            return list[1]
        elif len(list)==1:
            return list[0]
        else:
            return list[2]