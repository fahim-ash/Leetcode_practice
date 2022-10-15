// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        list1=[]
        list2=[]
        for i in nums:
            if i!=0:
                list1.append(i)
            else:
                list2.append(i)
        for j in list2:
            list1.append(j)
        nums.clear()
        for i in list1:
            nums.append(i)

        
        
        