// https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        z=''
        for i in num:
            z+=str(i)
        z=int(z)+k

        z=str(z)
        
        list=[]
        for i in z:
            list.append(i)
            
        return list    
        