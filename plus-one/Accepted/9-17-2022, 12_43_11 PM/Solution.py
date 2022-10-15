// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        z=""
        for i in digits:
            z+=str(i)
        z=int(z)+1  
        
        return [i for i in str(z)]
    