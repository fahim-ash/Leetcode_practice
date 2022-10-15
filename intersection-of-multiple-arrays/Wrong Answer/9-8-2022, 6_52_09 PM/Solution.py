// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        list=[0]
        for i in nums[0]:
            for j in range (len(nums)-1):
                if i in nums[j] and i in nums[j+1]:
                    if i>list[-1] and j not in list:
                        list.append(i)
                
        
        
        return (list[1:])
        
        