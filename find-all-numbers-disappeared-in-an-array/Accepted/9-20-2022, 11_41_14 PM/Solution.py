// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        z=set(nums)
        m=[]
        for i in range(1,len(nums)+1):
            if i not in z:
                m.append(i)
                
                
        return m
                
        