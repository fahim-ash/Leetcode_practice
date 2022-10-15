// https://leetcode.com/problems/sum-of-unique-elements

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=0
        list1=[]
        list2=[]
        for i in nums:
            if i not in list1:
                list1.append(i)
            else:
                list2.append(i)
                print(list2)
        for j in list2:
            if j in list1:
                list1.remove(j)
        for i in list1:
            count=count+i
        print(list1)
        return count
            