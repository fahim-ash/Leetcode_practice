// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        z=permutations(nums)
        m=[]
        for i in z:
            m.append(i)
            
        return m
        