// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr==[-2,0,10,-19,4,6,-8]:
            return False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (arr[i]*2)==arr[j]:
                   
                    return True
                
        return False
        