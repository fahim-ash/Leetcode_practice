// https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list=[]
        a=arr2[0]
        for i in arr2:
            for j in range(len(arr1)):
                if i==arr1[j]:
                    list.append(i)
                
        list2=[]   
        for j in arr1:
            if j not in list:
                
                list2.append(j)
        list2.sort()    
        return list+list2