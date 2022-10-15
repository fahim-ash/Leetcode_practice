// https://leetcode.com/problems/valid-boomerang

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        count=abs(points[0][0]-points[0][1])
        
        
        z=[]
        
        for i in points:
            print(z)
            if i not in z:
                z.append(i)
            else:
                return False
        for i in points:
            
            
            if count!= abs(i[0]-i[1]):
                return True
        return False
            
        