// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        list=[0]
        for i in nums[0]:
            if i in nums[1] and i in nums[2]:
                if i>list[-1]:
                    list.append(i)
                
        
        
        return (list[1:])
        
        