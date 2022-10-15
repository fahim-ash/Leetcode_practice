// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        z=arr
        z.sort()
        list=[]
        for i in range(len(arr)-1):
            if z[i]==z[i+1]:
                list.append(z[i])
        for i in z:
            for j in z:
                if j in list:
                    arr.remove(j)
        newList=[]

        if len(arr)<k:
            return ""
        else:
            for i in arr:
                if i not in list:
                    arr.remove(i)
                    return arr[0] 
        
       